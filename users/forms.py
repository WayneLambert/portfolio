from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class InactiveUserFound(Exception):
    """ Custom exception raised when inactive candidate tries to sign up """


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username'].lower().strip()
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].casefold().strip()
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        data = self.cleaned_data
        user = User(username=data['username'], email=data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data['username'].lower().strip()
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].casefold().strip()
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'author_view']

        widgets = {
            'author_view': forms.RadioSelect(attrs={
                'class': 'custom-control-inline',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
