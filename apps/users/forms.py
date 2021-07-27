from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from django_otp.plugins.otp_totp.models import TOTPDevice
from two_factor.forms import TOTPDeviceForm
from two_factor.utils import totp_digits


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        return self.cleaned_data['username'].casefold().strip()

    def clean_email(self):
        return self.cleaned_data['email'].strip()

    def clean_first_name(self):
        return self.cleaned_data['first_name'].title().strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].title().strip()

    def clean_password1(self):
        return self.cleaned_data['password1']

    def clean_password2(self):
        return self.cleaned_data['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        return self.cleaned_data['username'].casefold().strip()

    def clean_email(self):
        return self.cleaned_data['email'].casefold().strip()

    def clean_first_name(self):
        return self.cleaned_data['first_name'].title().strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].title().strip()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'author_view']
        widgets = {
            'author_view': forms.RadioSelect(attrs={
                'class': 'form-check-inline',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserTOTPDeviceForm(TOTPDeviceForm):

    token = forms.IntegerField(label=_("Token"), min_value=0, max_value=int('9' * totp_digits()))

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
        self.fields['token'].label = False
        self.fields["token"].widget.attrs={
            "autofocus": "autofocus",
            "inputmode": "numeric",
            "autocomplete": "one-time-code",
            "class": "form-control",
            "placeholder": "Enter token from authenticator app...",
        }

    def clean_token(self):
        return self.cleaned_data['token']

    def save(self):
        return TOTPDevice.objects.create(
            user=self.user,
            key=self.key,
            tolerance=self.tolerance,
            t0=self.t0,
            step=self.step,
            drift=self.drift,
            digits=self.digits,
            name='default'
        )


