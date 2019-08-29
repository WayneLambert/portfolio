from ab_back_end.settings import (
    SECRET_KEY,
    INSTALLED_APPS,
    CKEDITOR_UPLOAD_PATH,
    STATIC_URL,
    ROOT_URLCONF,
    TEMPLATES,
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST': {},
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
