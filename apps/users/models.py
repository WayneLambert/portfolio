from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from django_otp.util import random_hex
from encrypted_model_fields.fields import EncryptedCharField

from apps.users.utils import get_challenge_expiration_timestamp, token_validator


class Profile(models.Model):
    class AuthorView(models.IntegerChoices):
        USERNAME = 0
        FULL_NAME = 1

    slug = models.SlugField(max_length=255, unique=True)
    author_view = models.IntegerField(choices=AuthorView.choices, default=0)
    profile_picture = models.ImageField(
        default="profile_pics/default-user.jpg", upload_to="profile_pics", max_length=200
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)

    # Relationship Fields
    user = models.OneToOneField(
        get_user_model(), primary_key=True, related_name="profile", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.user.get_username()})"

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
            return self.user.get_username()
        else:
            return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("blog:users:profile", kwargs={"username": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify(self.user.get_username())
        super().save(*args, **kwargs)

    @property
    def is_two_factor_auth_by_token(self) -> bool:
        """ " Returns whether user is authenticated by token"""
        return self.user.totpdevice_set.exists()

    @property
    def is_two_factor_auth_by_email(self) -> bool:
        """ " Returns whether user is authenticated by email"""
        try:
            user_email_token = self.user.user_email_tokens.latest("id")
        except ObjectDoesNotExist:
            return False
        else:
            challenge_completed = user_email_token.challenge_completed
            token_within_expiry = user_email_token.is_token_within_expiry
            return bool(challenge_completed and token_within_expiry)

    @property
    def is_two_factor_authenticated(self) -> bool:
        """ " Returns whether user is authenticated by either token or email"""
        return bool(self.is_two_factor_auth_by_token or self.is_two_factor_auth_by_email)


class EmailToken(models.Model):
    challenge_email_address = models.EmailField()
    challenge_token = EncryptedCharField(
        max_length=255, default=random_hex, validators=[token_validator]
    )
    challenge_generation_timestamp = models.DateTimeField(
        null=True, blank=True, auto_now_add=True, editable=False
    )
    challenge_expiration_timestamp = models.DateTimeField(
        null=True, blank=True, default=get_challenge_expiration_timestamp
    )
    challenge_completed = models.BooleanField(default=False)
    challenge_completed_timestamp = models.DateTimeField(null=True, blank=True)
    token_expiration_timestamp = models.DateTimeField(null=True, blank=True)

    # Relationship Fields
    user = models.ForeignKey(
        get_user_model(), related_name="user_email_tokens", on_delete=models.CASCADE
    )

    def __repr__(self):
        return f"<EmailToken(id={self.id}, user_id={self.user_id}, user='{self.user}')>"

    def __str__(self):
        return self.__repr__()

    def save(self, *args, **kwargs):
        if not self._state.adding and self.challenge_completed:
            self.challenge_completed_timestamp = timezone.now()
            self.token_expiration_timestamp = timezone.now() + timedelta(
                seconds=settings.EMAIL_TOKEN_EXPIRATION_IN_SECS
            )
            self.challenge_expiration_timestamp = self.token_expiration_timestamp
        return super().save(*args, **kwargs)

    @property
    def is_challenge_within_expiry(self) -> bool:
        """ "
        Returns whether email token is within its challenge expiration date
        """
        if not self.challenge_expiration_timestamp:
            return False
        return timezone.now() <= self.challenge_expiration_timestamp

    @property
    def is_token_within_expiry(self) -> bool:
        """ "
        Returns whether email token is within its token expiration date
        """
        if not self.token_expiration_timestamp:
            return False
        return timezone.now() <= self.token_expiration_timestamp
