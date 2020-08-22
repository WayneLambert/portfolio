# pylint: disable=unused-import
import os

from aa_project.settings.base import (AWS_BASE_BUCKET_ADDRESS, BASE_DIR,
                                      DEFAULT_FROM_EMAIL_SES, INSTALLED_APPS,
                                      ROOT_URLCONF, SECRET_KEY, SITE_ID, STATIC_URL,
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

PYTEST_TEST_PASSWORD = os.environ['PYTEST_TEST_PASSWORD']
