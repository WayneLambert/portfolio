import os
import sys

import dj_database_url
from django.conf.global_settings import (EMAIL_BACKEND,
                                         SECURE_BROWSER_XSS_FILTER,
                                         SECURE_HSTS_INCLUDE_SUBDOMAINS,
                                         SECURE_HSTS_PRELOAD,
                                         SECURE_HSTS_SECONDS,
                                         SECURE_PROXY_SSL_HEADER)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if os.environ['SECRET_KEY']:
    SECRET_KEY = os.environ['SECRET_KEY']
else:
    print(""" A secret key needs to be set as an environment variable within
        the project's .env file. Remember that this should be listed
        in the project's .gitignore file.""")
    sys.exit(1)

# Additional field to adjust the login point for the Admin site
ADMIN_ALIAS = os.environ['ADMIN_ALIAS']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', False)))

# Gets Django web host for development purposes
DJANGO_WEBHOST = os.getenv('DJANGO_WEB_HOST', default='localhost')

# Gets Django database host for development purposes
DB_HOST = os.getenv('DJANGO_DB_HOST', default='localhost')

ALLOWED_HOSTS = [
    # Linode
    'waynelambert.co.uk',
    '178.79.156.225',
    # Heroku
    'wl-portfolio.herokuapp.com',
    'waynelambert.dev',
    'www.waynelambert.dev',
    # Local development
    '172.31.0.4',
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Third Party
    'rest_framework',
    'guardian',
    'crispy_forms',
    'corsheaders',
    'bootstrap4',
    'ckeditor',
    'ckeditor_uploader',
    'allauth',
    'allauth.account',
    'storages',

    # Project Apps
    'api.apps.ApiConfig',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'scraping.apps.ScrapingConfig',
    'count.apps.WordcountConfig',
    'contacts.apps.ContactsConfig',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Third party
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Third party
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ab_back_end.urls'

# Django Debug Toolbar Settings
if DEBUG:
    # For Django Debug Toolbar to be used in local development environment
    INSTALLED_APPS += ('debug_toolbar',)
    INTERNAL_IPS = ['127.0.0.1', '172.24.0.1']
    # For Django Debug Toolbar to be used in local dockerized development environment
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
    }
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
    SHOW_TOOLBAR_CALLBACK = True

# Production Settings
if not DEBUG:
    # Changes suggested from $ python3 manage.py check --deploy
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'ab_back_end/templates/'),
            os.path.join(BASE_DIR, 'ab_back_end/templates/admin/'),
            os.path.join(BASE_DIR, 'ab_back_end/templates/rest_framework/'),
            'blog/templates/blog/',
            'users/templates/users/',
            'users/templates/registration/',
            'scraping/templates/scraping/',
            'count/templates/count/',
            'contacts/templates/contacts/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ab_back_end.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_DOCKER_POSTGRES_SERVICE'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication backends setup for Django Guardian
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'blog/static'),
    os.path.join(BASE_DIR, 'count/static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media Files
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_IMAGES_ROOT = os.path.join(BASE_DIR, 'media/ab_back_end/static/default_images')

# Logging Configuration
# if DEBUG:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             },
#         },
#     }
# else:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'file': {
#                 'level': 'DEBUG',
#                 'class': 'logging.FileHandler',
#                 'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#             },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['file'],
#                 'level': 'DEBUG',
#                 'propagate': True,
#             },
#         },
#     }


# CK Editor Settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike',
                'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['RemoveFormat', 'CodeSnippet'],
        ],
        'extraPlugins': 'codesnippet',
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django-allauth Config
SITE_ID = 1
LOGIN_REDIRECT_URL = 'blog-home'
LOGOUT_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

# if HEROKU_DEPLOY:
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Django SES Email Backend Settings
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

if not DEBUG:
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'Wayne Lambert <admin@waynelambert.dev>'

# Django Storages Settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_DEFAULT_ACL = None
