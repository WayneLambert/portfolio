from django.forms import ModelForm, EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
