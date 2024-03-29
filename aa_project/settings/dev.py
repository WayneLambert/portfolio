# ruff: noqa: F403, F405

from aa_project.settings.base import *


DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
]

# For Django Debug Toolbar and Django Extensions to be used in development
INSTALLED_APPS += (
    "debug_toolbar",
    "django_extensions",
)

# Django Debug Toolbar Settings
INTERNAL_IPS = ["127.0.0.1", "172.24.0.1"]

# For Django Debug Toolbar to be used in local Dockerized development environment
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG}

# Additional Middleware
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]
SHOW_TOOLBAR_CALLBACK = True


# Do not log static request files to the console
def skip_static_requests(record):
    return not str(record.args[0]).startswith("GET /static/")


# Do not log debug request files to the console
def skip_debug_requests(record):
    return not str(record.args[0]).startswith("GET /__debug__/")


# Django Shell Plus Additional Imports
SHELL_PLUS_IMPORTS = [
    "import pathlib",
    "import sys",
    "import os",
    "import datetime",
    "import re",
    "import random",
    "import math",
    "import requests",
    "from bs4 import BeautifulSoup",
    "from rich import inspect, pretty, print",
    "from rich.console import Console",
]

# Logging Configuration (including colorised output from Rich)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "skip_static_requests": {
            "()": "django.utils.log.CallbackFilter",
            "callback": skip_static_requests,
        },
        "skip_debug_requests": {
            "()": "django.utils.log.CallbackFilter",
            "callback": skip_debug_requests,
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "rich": {"datefmt": "[%X]"},
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "level": "DEBUG",
            "filters": ["skip_static_requests", "skip_debug_requests", "require_debug_true"],
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "two_factor": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

# Simple Captcha Settings
SILENCED_SYSTEM_CHECKS = ["django_recaptcha.recaptcha_test_key_error"]

# Django Two-Factor Auth Settings
TWO_FACTOR_PATCH_ADMIN = False
TWO_FACTOR_CALL_GATEWAY = "two_factor.gateways.fake.Fake"
TWO_FACTOR_SMS_GATEWAY = "two_factor.gateways.fake.Fake"
