from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from two_factor.forms import TOTPDeviceForm
from two_factor.utils import totp_digits

from apps.users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_username(self):
        return self.cleaned_data["username"].casefold()

    def clean_first_name(self):
        return self.cleaned_data["first_name"].title()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].title()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]

    def clean_username(self):
        return self.cleaned_data["username"].casefold().strip()

    def clean_email(self):
        return self.cleaned_data["email"].casefold().strip()

    def clean_first_name(self):
        return self.cleaned_data["first_name"].title().strip()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].title().strip()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "author_view"]
        widgets = {
            "author_view": forms.RadioSelect(
                attrs={
                    "class": "form-check-inline",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserTOTPDeviceForm(TOTPDeviceForm):
    """Used during the setup of the QR Code"""

    def __init__(self, key, user, metadata=None, **kwargs):
        super().__init__(self, key, user, **kwargs)
        self.key = key
        self.tolerance = 1
        self.t0 = 0
        self.step = 30
        self.drift = 0
        self.digits = totp_digits()
        self.user = user
        self.metadata = metadata or {}

        self.helper = FormHelper()
        self.fields["token"].label = False
        extra_attrs = {
            "class": "login100-form validate-form textinput textInput form-control",
            "title": "",
            "placeholder": "Enter token from authenticator app...",
        }
        self.fields["token"].widget.attrs.update(extra_attrs)


class EmailTokenSubmissionForm(forms.Form):
    """Used during the setup or submission of an email token"""

    MIN_TOKEN_VALUE = 0
    MAX_TOKEN_VALUE = 999_999

    token = forms.IntegerField(min_value=MIN_TOKEN_VALUE, max_value=MAX_TOKEN_VALUE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = "email-token-submission"
        self.fields["token"].label = False
        self.fields["token"].widget.attrs = {
            "autofocus": "autofocus",
            "inputmode": "numeric",
            "autocomplete": "one-time-code",
            "class": "form-control",
            "title": "",
            "placeholder": "Enter token from email...",
            "min": self.MIN_TOKEN_VALUE,
            "max": self.MAX_TOKEN_VALUE,
        }
