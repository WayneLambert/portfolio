# pylint: disable=unused-import
from .settings import (BASE_DIR, CKEDITOR_UPLOAD_PATH, INSTALLED_APPS, ROOT_URLCONF,
                       SECRET_KEY, STATIC_URL, TEMPLATES)

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
