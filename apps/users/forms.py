from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from apps.users.models import Profile


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
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
