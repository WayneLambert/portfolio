# ruff: noqa: F403, F405

import dj_database_url

from aa_project.settings.base import *


DEBUG = False

ALLOWED_HOSTS = [
    "wl-portfolio.herokuapp.com",
    "waynelambert.dev",
    "www.waynelambert.dev",
]

# Changes suggested from $ python manage.py check --deploy
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_REFERRER_POLICY = "same-origin"

# Django Storages Settings
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Heroku Deployment Settings for Postgres
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES["default"].update(db_from_env)

# Simple Captcha Settings
RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]

# Django Two-Factor Auth Settings
TWO_FACTOR_LOGIN_TIMEOUT = 300
TWO_FACTOR_REMEMBER_COOKIE_AGE = 60 * 60 * 24 * 28
