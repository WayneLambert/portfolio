import datetime
import random

from django.conf import settings
from django.utils import timezone

from django_otp.util import hex_validator


def generate_token() -> str:
    """ Generates a 6 digit random number including any leading zeros """
    return str(random.randint(0, 999_999)).zfill(6)


def get_challenge_expiration_timestamp():
    """ Sets expiration timestamp at point in future as per the project setting """
    return timezone.now() + datetime.timedelta(seconds=settings.EMAIL_TOKEN_EXPIRATION_IN_SECS)


def token_validator(*args, **kwargs):
    """ Wraps hex_validator generator satisfying `makemigrations` """
    return hex_validator()(*args, **kwargs)
