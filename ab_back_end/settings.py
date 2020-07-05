import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

# Login URL for the Admin panel
ADMIN_ALIAS = os.environ['ADMIN_ALIAS']

DEBUG = bool(int(os.environ['DEBUG']))

ALLOWED_HOSTS = [
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
    'django.contrib.humanize',

    # Third Party
    'rest_framework',
    'guardian',
    'crispy_forms',
    'corsheaders',
    'bootstrap4',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    'captcha',
    'google_analytics',
    'widget_tweaks',

    # Project Apps
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'cv.apps.CvConfig',
    'contacts.apps.ContactsConfig',
    'countdown_letters.apps.CountdownLettersConfig',
    'countdown_numbers.apps.CountdownNumbersConfig',
    'text_analysis.apps.TextAnalysisConfig',
    'roulette.apps.RouletteConfig',
    'scraping.apps.ScrapingConfig',
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

if DEBUG:
    # For Django Debug Toolbar and Django Extensions to be used in development
    INSTALLED_APPS += (
        'debug_toolbar',
        'template_profiler_panel',
        'django_extensions',
    )

    # Django Debug Toolbar Settings
    INTERNAL_IPS = ['127.0.0.1', '172.24.0.1']

    # For Django Debug Toolbar to be used in local dockerized development environment
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
    }

    # Additional Middleware
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
        'template_profiler_panel.panels.template.TemplateProfilerPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
    SHOW_TOOLBAR_CALLBACK = True

    # Do not log static request files to the console
    def skip_static_requests(record):
        return not record.args[0].startswith('GET /static/')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'skip_static_requests': {
                '()': 'django.utils.log.CallbackFilter',
                'callback': skip_static_requests,
            }
        },
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            }
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'filters': ['skip_static_requests'],
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
        },
        'loggers': {
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
        }
    }

# Production Settings
if not DEBUG:
    # Changes suggested from $ python3 manage.py check --deploy
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 2592000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_REFERRER_POLICY = 'same-origin'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'ab_back_end/templates/'),
            os.path.join(BASE_DIR, 'ab_back_end/templates/admin/'),
            os.path.join(BASE_DIR, 'ab_back_end/templates/rest_framework/'),
            'pages/templates/pages/',
            'blog/templates/blog/',
            'cv/templates/cv/',
            'users/templates/users/',
            'users/templates/registration/',
            'contacts/templates/contacts/',
            'countdown_letters/templates/countdown_letters/',
            'countdown_numbers/templates/countdown_numbers/',
            'text_analysis/templates/text_analysis/',
            'roulette/templates/roulette/',
            'scraping/templates/scraping/',
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
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_IMAGES_ROOT = os.path.join(BASE_DIR, 'media/ab_back_end/static/default_images')

# CK Editor Settings
AWS_QUERYSTRING_AUTH = False
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar': 'Custom',
        'width': '100%',
        'height': '400',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'Size', 'Bold', 'Italic', 'Underline', 'Strike',
             'Undo', 'Redo'],
            ['Find', 'Replace'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['RemoveFormat', 'CodeSnippet', 'Maximize', 'Preview'],
        ],
        'extraPlugins': ['codesnippet', 'maximize'],
    }
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

# Heroku Deployment Settings
if not DEBUG:
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

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

# Simple Captcha Settings
if DEBUG:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
else:
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']

# Google Analytics
GOOGLE_ANALYTICS = {
    'google_analytics_id': os.environ['GA_TRACKING_ID'],
}

# For PyTest
if DEBUG:
    PYTEST_TEST_PASSWORD = os.environ['PYTEST_TEST_PASSWORD']
