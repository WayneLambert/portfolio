from aa_project.settings.base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
]

# For Django Debug Toolbar and Django Extensions to be used in development
INSTALLED_APPS += (
    'debug_toolbar',
    'template_profiler_panel',
    'django_extensions',
)

# Django Debug Toolbar Settings
INTERNAL_IPS = ['127.0.0.1', '172.24.0.1']

# For Django Debug Toolbar to be used in local Dockerized development environment
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
    'debug_toolbar.panels.profiling.ProfilingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
SHOW_TOOLBAR_CALLBACK = True

# Do not log static request files to the console
def skip_static_requests(record):
    return not str(record.args[0]).startswith('GET /static/')

# Django Shell Plus Additional Imports
SHELL_PLUS_IMPORTS = [
    'import re',
    'import requests',
    'from bs4 import BeautifulSoup',
    'from rich import pretty',
]

# Logging Configuration (including colorised output from Rich)
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
        'rich': {'datefmt': '[%X]'},
    },

    'handlers': {
        'console': {
            'class': 'rich.logging.RichHandler',
            'formatter': 'rich',
            'level': 'INFO',
            'filters': ['skip_static_requests'],
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# Simple Captcha Settings
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
