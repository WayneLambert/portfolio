import os
import sys

from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, APPS_DIR)

SECRET_KEY = os.environ['SECRET_KEY']

# Login path for the Django admin panel
DJANGO_ADMIN_LOGIN_PATH = os.environ['DJANGO_ADMIN_LOGIN_PATH']

# Applications supplementing Django's core functionality
DJANGO_THIRD_PARTY_AUX_APPS = [
    'whitenoise.runserver_nostatic',
]

# Applications supplied within Django core
DEFAULT_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]

# Additional third party applications
THIRD_PARTY_APPS = [
    'rest_framework',
    'guardian',
    'crispy_forms',
    'bootstrap4',
    'storages',
    'captcha',
    'widget_tweaks',
    'tinymce',
]

# Project Apps
PROJECT_APPS = [
    'apps.api.apps.ApiConfig',
    'apps.blog.apps.BlogConfig',
    'apps.contacts.apps.ContactsConfig',
    'apps.countdown_letters.apps.CountdownLettersConfig',
    'apps.countdown_numbers.apps.CountdownNumbersConfig',
    'apps.cv.apps.CvConfig',
    'apps.pages.apps.PagesConfig',
    'apps.roulette.apps.RouletteConfig',
    'apps.scraping.apps.ScrapingConfig',
    'apps.text_analysis.apps.TextAnalysisConfig',
    'apps.users.apps.UsersConfig',
]

INSTALLED_APPS = DJANGO_THIRD_PARTY_AUX_APPS + DEFAULT_DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Third party
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Project's root URL configuration
ROOT_URLCONF = 'aa_project.urls'

# Django Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'aa_project/templates/'),
            os.path.join(BASE_DIR, 'aa_project/templates/admin/'),
            os.path.join(BASE_DIR, 'aa_project/templates/rest_framework/'),
            os.path.join(APPS_DIR, 'pages/templates/pages/'),
            os.path.join(APPS_DIR, 'blog/templates/blog/'),
            os.path.join(APPS_DIR, 'contacts/templates/contacts/'),
            os.path.join(APPS_DIR, 'countdown_letters/templates/countdown_letters/'),
            os.path.join(APPS_DIR, 'countdown_numbers/templates/countdown_numbers/'),
            os.path.join(APPS_DIR, 'cv/templates/cv/'),
            os.path.join(APPS_DIR, 'users/templates/users/'),
            os.path.join(APPS_DIR, 'users/templates/registration/'),
            os.path.join(APPS_DIR, 'roulette/templates/roulette/'),
            os.path.join(APPS_DIR, 'scraping/templates/scraping/'),
            os.path.join(APPS_DIR, 'text_analysis/templates/text_analysis/'),
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

# Location of Project's WSGI application
WSGI_APPLICATION = 'aa_project.wsgi.application'

# Database Configuration
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
    'guardian.backends.ObjectPermissionBackend',
)


# Internationalization
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
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_IMAGES_ROOT = os.path.join(BASE_DIR, 'media/aa_project/static/default_images')

# Tiny MCE Editor Config
TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'height': '800px',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'selector': 'textarea',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen insertdatetime nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists charmap print hr
            anchor pagebreak spellchecker emoticons help
            ''',
    'toolbar1': '''
            fontselect fontsizeselect | bold italic underline | blockquote |
            forecolor backcolor | alignleft alignright aligncenter alignjustify |
            indent outdent
            ''',
    'toolbar2': '''
            bullist numlist | table |
            visualblocks visualchars | searchreplace |
            hr pagebreak nonbreaking anchor | link image media |
            codesample | code | charmap emoticons | pre fullscreen preview
            ''',
    'codesample_global_prismjs': True,
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'},
        {'text': 'HTML/XML', 'value': 'html'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'Docker', 'value': 'docker'},
        {'text': 'Bash', 'value': 'bash'},
        {'text': 'SHELL', 'value': 'shell'},
        {'text': 'Git', 'value': 'git'},
        {'text': 'Markdown', 'value': 'markdown'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'SQL', 'value': 'sql'},
        {'text': 'Json', 'value': 'json'},
        {'text': 'Diff', 'value': 'diff'},
        {'text': 'Ruby', 'value': 'ruby'},
        {'text': 'YAML', 'value': 'yaml'},
        {'text': 'TOML', 'value': 'toml'},
    ],
    "font_formats":
        "Ubuntu Mono='Ubuntu Mono', monospace; sans-serif; Arial=arial,helvetica,sans-serif; Tahoma=tahoma,arial,helvetica,sans-serif; Verdana=verdana,geneva; Courier New=courier new,courier,monospace",
}


CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 3,
}

SITE_ID = 1
LOGIN_URL = 'blog:users:login'
LOGIN_REDIRECT_URL = 'blog:home'
LOGOUT_REDIRECT_URL = 'blog:home'


# Django SES Email Backend Settings
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'
EMAIL_HOST_SES = os.environ['EMAIL_HOST_SES']
EMAIL_HOST_USER_SES = os.environ['EMAIL_HOST_USER_SES']
EMAIL_HOST_PASSWORD_SES = os.environ['EMAIL_HOST_PASSWORD_SES']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL_SES = os.environ['DEFAULT_FROM_EMAIL_SES']

# Django Storages Settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_DEFAULT_ACL = None
AWS_BASE_BUCKET_ADDRESS = os.environ['AWS_BASE_BUCKET_ADDRESS']
