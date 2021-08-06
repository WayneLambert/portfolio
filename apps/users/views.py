from typing import Any, Dict

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail.message import EmailMultiAlternatives
from django.http.request import split_domain_port
from django.shortcuts import get_object_or_404, redirect, reverse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateView

from shapeshifter.views import MultiModelFormView
from two_factor.forms import AuthenticationTokenForm
from two_factor.views.core import LoginView, SetupView
from users.utils import generate_token, get_challenge_expiration_timestamp

from apps.users.forms import (EmailTokenSubmissionForm, ProfileUpdateForm,
                              UserRegisterForm, UserTOTPDeviceForm, UserUpdateForm,)
from apps.users.models import EmailToken, Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:users:setup')
    USER_ALREADY_EXISTS_MSG = """
        The username you've attempted to register with is already taken.
        Perhaps you already have an account? If so, you can log in using
        the link below, or register using a alternative username.
    """

    def user_exists(self) -> bool:
        username = self.request.POST['username']
        user = get_user_model().objects.filter(username=username)
        if user.exists():
            return True

    def form_valid(self, form):
        self.object = form.save()
        form_valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user=user, backend=backend)
        return form_valid

    def form_invalid(self, form):
        if self.user_exists():
            messages.error(self.request, message=self.USER_ALREADY_EXISTS_MSG)
            return redirect(reverse('blog:users:register'))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_list = (
        ('auth', AuthenticationForm),
        ('token', AuthenticationTokenForm),
    )


class UserSetupQRView(SetupView):
    template_name = 'two_factor/setup_by_qr.html'
    success_url = 'blog:home'

    form_list = (
        ('generator', UserTOTPDeviceForm),
    )
    condition_dict = {
        'generator': lambda self: True,
    }

    def get_method(self):
        return 'generator'


class UserSetupEmailView(TemplateView):
    template_name = 'two_factor/setup_by_email.html'
    success_url = 'blog:users:setup_email_token'

    def store_token_in_db(self, user, token):
        """ Creates an email token onbject in the DB """
        EmailToken.objects.create(
            challenge_email_address=user.email,
            challenge_token=token,
            challenge_generation_timestamp=timezone.now(),
            challenge_expiration_timestamp=get_challenge_expiration_timestamp(),
            challenge_completed=False,
            user_id=user.id
        )

    def build_html_content(self, user, token):
        """" Specifies the email template and context variables """
        return render_to_string(
            template_name='emails/token.html',
            context={
                'user': user,
                'token': token,
            }
        )

    def email_two_factor_token(self, user: get_user_model(), token) -> None:
        """ Sends email containing one-time token """

        subject = "Your One Time Token"
        msg = EmailMultiAlternatives(
            subject=subject,
            body=self.build_html_content(user, token),
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            to=[user.email],
        )
        msg.content_subtype = 'html'
        msg.mixed_subtype = 'related'
        msg.send()


    def post(self, request, *args, **kwargs):
        """ Master func handling the user clicking the `Send Token by Email` button """
        token = generate_token()
        user = request.user
        self.store_token_in_db(user, token)
        self.email_two_factor_token(user, token)
        return redirect(self.success_url)


class UserSetupEmailTokenView(TemplateView):

    model = EmailToken
    template_name = 'two_factor/setup_email_token.html'
    success_url = reverse_lazy('blog:home')

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        email = self.request.user.email.strip()
        domain = email.split('@')[-1]
        context['form'] = EmailTokenSubmissionForm(self.request.POST or None)
        context['user_email'] = f"{email[0:2]}{'**********@'}{domain}"
        return context

    def get_email_token(self) -> str:
        email_token = EmailToken.objects.filter(user_id=self.request.user.id).latest('id')
        return email_token.challenge_token

    def get_challenge_returned(self) -> str:
        return str(self.request.POST['challenge_token_returned'].strip())

    def does_challenge_pass(self, token_returned) -> bool:
        token_to_match = self.get_email_token()
        return token_returned == token_to_match

    def is_token_within_expiry(self) -> bool:
        email_token = EmailToken.objects.filter(user_id=self.request.user.id).latest('id')
        return timezone.now() <= email_token.challenge_expiration_timestamp

    def update_db(self, user):
        email_token = EmailToken.objects.filter(user_id=user.id).latest('id')
        email_token.challenge_completed_timestamp=timezone.now(),
        email_token.challenge_completed=True
        email_token.save()

    def populate_message(self, challenge_passes, token_within_expiry):
        if not challenge_passes:
            msg = (
                "The token you have entered is incorrect.<br /><br />" +
                "Please re-check the code and try again."
            )
            messages.add_message(self.request, messages.INFO, mark_safe(msg))
        elif not token_within_expiry:
            msg = (
                "The 5 minute expiration time has elapsed.<br /><br />" +
                "Use the 'still no code?' link below to generate a new token " +
                "which you will receive by email. Then re-enter the new code above."
            )
            messages.add_message(self.request, messages.INFO, mark_safe(msg))

    def post(self, request, *args, **kwargs):
        token_returned = self.get_challenge_returned()
        challenge_passes = self.does_challenge_pass(token_returned)
        token_within_expiry = self.is_token_within_expiry()
        if challenge_passes and token_within_expiry:
            self.update_db(request.user)
            return redirect(self.success_url)
        self.populate_message(challenge_passes, token_within_expiry)
        return redirect('blog:users:setup_email_token')


class ProfileView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), username=self.kwargs['username'])


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, MultiModelFormView):
    """
    Any user attempting to GET the profile update page of another user,
    whether present in the DB or not, will receive a 403 error.
    """
    form_classes = (UserUpdateForm, ProfileUpdateForm)
    template_name = 'users/profile_update.html'

    def test_func(self) -> bool:
        return self.request.user.username == self.kwargs['username']

    def get_instances(self) -> dict:
        return {
            'userupdateform': self.request.user,
            'profileupdateform': self.request.user.user
        }

    def get_success_url(self):
        return reverse_lazy(
            'blog:users:profile', kwargs={'username': self.request.user.username})
