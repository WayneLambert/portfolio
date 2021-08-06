from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from two_factor.forms import TOTPDeviceForm
from two_factor.utils import totp_digits

from apps.users.models import EmailToken, Profile


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
        self.fields['token'].widget.attrs={
            'autofocus': 'autofocus',
            'inputmode': 'numeric',
            'autocomplete': 'one-time-code',
            'class': 'form-control',
            'title': '',
            'placeholder': 'Enter token from authenticator app...',
        }


class EmailTokenSubmissionForm(forms.ModelForm):
    challenge_token_returned = forms.CharField(label=_(""))

    class Meta:
        model = EmailToken
        fields = ['challenge_token_returned', ]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'challenge-token-returned'
        self.fields['challenge_token_returned'].label = False
        self.fields['challenge_token_returned'].widget.attrs={
            'autofocus': 'autofocus',
            'inputmode': 'numeric',
            'autocomplete': 'one-time-code',
            'class': 'form-control',
            'title': '',
            'placeholder': 'Enter token from email...',
        }
