from typing import Any, Dict

from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DetailView, TemplateView
from django.views.generic.edit import FormView

from shapeshifter.views import MultiModelFormView
from two_factor.forms import AuthenticationTokenForm
from two_factor.views.core import LoginView, SetupView
from users.mixins import TwoFactorAuthUserMixin
from users.utils import generate_token, get_challenge_expiration_timestamp

from apps.users.forms import (
    EmailTokenSubmissionForm,
    ProfileUpdateForm,
    UserRegisterForm,
    UserTOTPDeviceForm,
    UserUpdateForm,
)
from apps.users.models import EmailToken, Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("blog:users:setup")
    register_url = reverse_lazy("blog:users:register")
    html_msg = """
        The username you've attempted to register with is already taken.<br /><br />
        Perhaps you already have an account? If so, you can log in using
        the link below, or register using a alternative username.
    """

    def user_exists(self, form) -> bool:
        username = form.data["username"]
        user = get_user_model().objects.filter(username=username)
        if user.exists():
            return True

    def form_valid(self, form):
        self.object = form.save()
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = auth.authenticate(username=username, password=password)
        backend = "django.contrib.auth.backends.ModelBackend"
        auth.login(self.request, user=user, backend=backend)
        return form_valid

    def form_invalid(self, form):
        if self.user_exists(form):
            messages.error(self.request, mark_safe(self.html_msg))
            return redirect(self.register_url)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    two_factor_setup_url = reverse_lazy("blog:users:setup")
    two_factor_setup_email_url = reverse_lazy("blog:users:setup_email")
    form_list = (
        ("auth", AuthenticationForm),
        ("token", AuthenticationTokenForm),
    )

    def _add_user_does_not_exist_message(self):
        """Constructs a message for the UI"""
        html_msg = (
            "The username you've attempted to log in with does not exist.<br /><br />"
            + "Please re-check the username and try again."
        )
        messages.info(self.request, mark_safe(html_msg))

    def _add_incorrect_password_message(self):
        """Constructs a message for the UI"""
        html_msg = (
            "Please enter a correct username and password.<br /><br />"
            + "Note that both fields may be case-sensitive."
        )
        messages.error(self.request, mark_safe(html_msg))

    def retrieve_token_from_db(self, user) -> EmailToken:
        """Retrieves the latest email token for the user from the DB"""
        return EmailToken.objects.filter(user_id=user.id).latest("id")

    def build_html_content(self, user, token) -> str:
        """ " Specifies the email template and context variables"""
        return render_to_string(
            template_name="emails/token.html",
            context={
                "user": user,
                "token": token,
            },
        )

    def email_two_factor_token(self, user: get_user_model(), token):
        """Sends email containing current token"""

        subject = "Your One Time Token"
        msg = EmailMultiAlternatives(
            subject=subject,
            body=self.build_html_content(user, token),
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            to=[user.email],
        )
        msg.content_subtype = "html"
        msg.mixed_subtype = "related"
        msg.send()

    def _get_credentials(self, user) -> Dict[str, Any]:
        """Gets the credentials of the user being attempted"""
        return {
            "username": user.get_username(),
            "password": self.storage.request._post["auth-password"],
        }

    def is_password_correct(self, user, credentials) -> bool:
        """Checks the password entered by the user passes authentication check"""
        return bool(check_password(credentials["password"], user.password))

    def authenticate_user(self, user):
        """
        Manually authenticates the user or calls for the creation of
        an incorrect password message
        """
        credentials = self._get_credentials(user)
        password_valid = self.is_password_correct(user, credentials)
        if not password_valid and self.request.user.is_anonymous:
            return self._add_incorrect_password_message()
        username = credentials["username"]
        password = credentials["password"]
        return auth.authenticate(request=self.request, username=username, password=password)

    def login_user(self, user):
        """Logs in the already authenticated user"""
        backend = "django.contrib.auth.backends.ModelBackend"
        auth.login(self.request, user=user, backend=backend)

    def handle_email_auth_user(self, user):
        """Handles the actions for processing an email authenticated user"""
        user_passes_auth = self.authenticate_user(user=user)
        if user_passes_auth:
            self.login_user(user=user)
            token = self.retrieve_token_from_db(user)
            self.email_two_factor_token(user, token)
            return redirect("blog:users:setup_email_token")
        return redirect(self.request.path_info)

    def post(self, *args, **kwargs):
        """
        Processes POST request in accordance with documented scenarios.

        Where the user has opted for the device token method, the Django
        Two-Factor Auth package handles implementation. Where the user
        uses email, the project code handles it.
        """

        if self.steps.current == "auth":
            username = self.storage.request._post["auth-username"]

            # Scenario 1: The user does not exist in the DB
            try:
                user = get_user_model().objects.get(username=username)
            except get_user_model().DoesNotExist:
                self._add_user_does_not_exist_message()
                return redirect(self.request.path_info)

            # Scenario 2: The user exists but is not set up for valid 2FA at all.
            # This includes users that now have an expired email token
            if not user.profile.is_two_factor_authenticated:
                super().post(*args, **kwargs)
                self.authenticate_user(user=user)
                return redirect(self.two_factor_setup_url)

            # Scenario 3: The user exists and is using the device token method of 2FA
            elif user.profile.is_two_factor_auth_by_token:
                self.storage.reset()
                self.authenticate_user(user=user)
                return super().post(*args, **kwargs)

            # Scenario 4: The user is authenticating with an unexpired email token
            elif user.profile.is_two_factor_auth_by_email:
                return self.handle_email_auth_user(user)

        # If at the token step of the login wizard and the user uses the token method,
        # enable the Django Two-Factor Auth package to handle
        elif self.steps.current == "token":
            user_pk = self.request.session["wizard_user_login_view"]["user_pk"]
            user = get_user_model().objects.get(pk=user_pk)
            if user.profile.is_two_factor_auth_by_token:
                return super().post(*args, **kwargs)


class UserSetupQRView(SetupView):
    template_name = "two_factor/setup_by_qr.html"
    success_url = reverse_lazy("blog:home")

    form_list = (("generator", UserTOTPDeviceForm),)
    condition_dict = {
        "generator": lambda self: True,
    }

    def get_method(self):
        return "generator"


class UserSetupEmailView(TemplateView):
    template_name = "two_factor/setup_by_email.html"
    success_url = reverse_lazy("blog:users:setup_email_token")

    def store_token_in_db(self, user: get_user_model(), token: str):
        """Creates an email token object in the DB"""
        EmailToken.objects.create(
            challenge_email_address=user.email,
            challenge_token=token,
            challenge_generation_timestamp=timezone.now(),
            challenge_expiration_timestamp=get_challenge_expiration_timestamp(),
            challenge_completed=False,
            user_id=user.id,
        )

    def build_html_content(self, user: get_user_model(), token: str) -> str:
        """ " Specifies the email template and context variables"""
        return render_to_string(
            template_name="emails/token.html",
            context={
                "user": user,
                "token": token,
                "setup": True,
            },
        )

    def email_two_factor_token(self, user: get_user_model(), token: str):
        """Sends email containing one-time token"""

        subject = "Your One Time Token"
        msg = EmailMultiAlternatives(
            subject=subject,
            body=self.build_html_content(user, token),
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            to=[user.email],
        )
        msg.content_subtype = "html"
        msg.mixed_subtype = "related"
        msg.send()

    def post(self, request, *args, **kwargs):
        """Master func handling the user clicking the `Send Token by Email` button"""
        token = generate_token()
        user = request.user
        self.store_token_in_db(user, token)
        self.email_two_factor_token(user, token)
        return redirect(self.success_url)


class UserSetupEmailTokenView(FormView):
    template_name = "two_factor/setup_email_token.html"
    form_class = EmailTokenSubmissionForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """
        Facilitates a custom token submission form in addition to a
        partly redacted version of the email address and the user's
        first name to be passed through to the template's context.
        """
        context = super().get_context_data(user=self.request.user, **kwargs)
        email = self.request.user.email.strip()
        domain = email.split("@")[-1]
        context["user_first_name"] = self.request.user.get_short_name()
        context["redacted_user_email"] = f"{email[0:2]}**********@{domain}"
        return context

    def get_email_token(self) -> EmailToken:
        """Retrieves the latest email token from the DB for the user"""
        return EmailToken.objects.filter(user_id=self.request.user.id).latest("id")

    def does_challenge_pass(self, token_returned) -> bool:
        """Evaluates whether the token input passes the challenge"""
        token_to_match = self.get_email_token().challenge_token
        return token_returned == token_to_match

    def update_db(self, email_token):
        """
        Updates the database to mark the challenge as being
        completed and calls the model's .save() method
        """
        email_token.challenge_completed = True
        email_token.save()

    def build_html_content(self, user, token) -> str:
        """ " Specifies the email template and context variables"""
        return render_to_string(
            template_name="emails/success.html",
            context={
                "user": user,
                "token": token,
                "setup": True,
            },
        )

    def email_two_factor_success(self, user: get_user_model(), token):
        """Sends email containing one-time token"""

        subject = "Two-Factor Authentication Successful"
        msg = EmailMultiAlternatives(
            subject=subject,
            body=self.build_html_content(user, token),
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            to=[user.email],
        )
        msg.content_subtype = "html"
        msg.mixed_subtype = "related"
        msg.send()

    def populate_message(self, challenge_passes, token_within_expiry):
        """
        Creates a customised version of the message to give the user
        interactive feedback on their input.
        """
        if not challenge_passes:
            msg = (
                "The token you have entered is incorrect.<br /><br />"
                + "Please re-check the code and try again."
            )
            messages.add_message(self.request, messages.INFO, mark_safe(msg))
        elif not token_within_expiry:
            msg = (
                "The 5 minute expiration time has elapsed.<br /><br />"
                + "Use the 'still no code?' link below to generate a new token "
                + "which you will receive by email. Then re-enter the new code above."
            )
            messages.add_message(self.request, messages.INFO, mark_safe(msg))

    def form_valid(self, form):
        super().form_valid(form)
        token_returned = str(form.cleaned_data["token"]).zfill(6)
        challenge_passes = self.does_challenge_pass(token_returned)
        email_token = self.get_email_token()
        if challenge_passes and email_token.is_challenge_within_expiry:
            self.update_db(email_token)
            self.email_two_factor_success(self.request.user, email_token)
            return redirect(self.success_url)
        self.populate_message(challenge_passes, email_token.is_challenge_within_expiry)
        return redirect("blog:users:setup_email_token")


class ProfileView(TwoFactorAuthUserMixin, DetailView):
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), username=self.kwargs["username"])


class ProfileUpdateView(TwoFactorAuthUserMixin, UserPassesTestMixin, MultiModelFormView):
    """
    Any user attempting to GET the profile update page of another user,
    whether present in the DB or not, will receive a 403 error.
    """

    form_classes = (UserUpdateForm, ProfileUpdateForm)
    template_name = "users/profile_update.html"

    def test_func(self) -> bool:
        return self.request.user.get_username() == self.kwargs["username"]

    def get_instances(self) -> Dict[str, Any]:
        return {
            "userupdateform": self.request.user,
            "profileupdateform": self.request.user.profile,
        }

    def get_success_url(self):
        username = self.request.user.get_username()
        return reverse("blog:users:profile", kwargs={"username": username})


class UserPasswordResetView(PasswordResetView):
    template_name = "users/password_reset_form.html"
    email_template_name = "users/password_reset_email.html"
    subject_template_name = "users/password_reset_subject.txt"
    success_url = reverse_lazy("blog:users:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("blog:users:password_reset_complete")


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"
