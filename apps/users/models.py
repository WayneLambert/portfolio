from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from django_cryptography.fields import encrypt
from django_otp.util import random_hex

from apps.users.utils import get_challenge_expiration_timestamp, token_validator


class Profile(models.Model):

    class AuthorView(models.IntegerChoices):
        USERNAME = 0
        FULL_NAME = 1

    slug = models.SlugField(max_length=255, unique=True)
    author_view = models.IntegerField(choices=AuthorView.choices, default=0)
    profile_picture = models.ImageField(
        default='profile_pics/default-user.jpg', upload_to='profile_pics', max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)

    # Relationship Fields
    user = models.OneToOneField(
        get_user_model(), primary_key=True, related_name='user', on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"

    @property
    def initials(self):
        inits = f"{self.user.first_name[0]}{self.user.last_name[0]}"
        return inits.upper().strip()

    @property
    def join_year(self) -> int:
        return self.user.date_joined.year

    @property
    def display_name(self):
        if self.author_view == 0:
            return self.user.username
        else:
            return self.full_name

    def get_absolute_url(self):
        return reverse('blog:users:profile', kwargs={'username': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


class EmailToken(models.Model):

    challenge_email_address = models.EmailField()
    challenge_token = encrypt(models.CharField(
        max_length=40, default=random_hex, validators=[token_validator]))
    challenge_generation_timestamp = models.DateTimeField(
        null=True, auto_now_add=True, editable=False)
    challenge_expiration_timestamp = models.DateTimeField(
        null=True, default=get_challenge_expiration_timestamp)
    challenge_completed = models.BooleanField(default=False)
    challenge_completed_timestamp = models.DateTimeField(null=True, auto_now=True)

    # Relationship Fields
    user = models.ForeignKey(
        get_user_model(), related_name='user_email_devices', on_delete=models.CASCADE)

    def __repr__(self):
        return f"<EmailDevice(id={self.id}, user={self.user})>"

    def __str__(self):
        return f"<EmailDevice(id={self.id}, user={self.user})>"
