# pylint: disable=unused-import
from .settings import (AWS_BASE_BUCKET_ADDRESS, BASE_DIR, DEFAULT_FROM_EMAIL_SES,
                       INSTALLED_APPS, ROOT_URLCONF, SECRET_KEY, SITE_ID, STATIC_URL,
                       TEMPLATES,)


# IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {},
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
