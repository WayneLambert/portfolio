# pylint: disable=unused-import
import os

from django.contrib.auth.hashers import BasePasswordHasher

from aa_project.settings.base import (AWS_BASE_BUCKET_ADDRESS, BASE_DIR,
                                      DEFAULT_FROM_EMAIL_SES, INSTALLED_APPS,
                                      ROOT_URLCONF, SECRET_KEY, SITE_ID, STATIC_URL,
                                      TEMPLATES,)


# Postgres Testing Database Configuration. Uses in-memory DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_DOCKER_POSTGRES_SERVICE'),
        'PORT': os.getenv('DB_PORT'),
        'TEST': {
            'NAME': 'test_portfolio_db',
        },
    }
}

# GitHub Actions Postgres
if os.environ['CI'] == True:
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'github_actions',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        },
        'TEST': {
            'NAME': 'test_portfolio_db',
        },
    }

# Ensures tests are never sending actual emails
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Ensures tests have access to a password for tests from the environment
PYTEST_TEST_PASSWORD = os.environ['PYTEST_TEST_PASSWORD']

# Override back to default storage since tests do not run `collectstatic`
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Eliminates warning about missing staticfiles directory
WHITENOISE_AUTOREFRESH = True

# A less secure password hasher used for testing to enable faster test runs
class SimplePasswordHasher(BasePasswordHasher):
    """
    A simple password hasher which is deliberately insecure since we do
    not care about the security of passwords being set during the
    running of tests.
    """

    algorithm = "dumb"  # This attribute is needed by the base class.

    def salt(self):
        return ""

    def encode(self, password, salt):
        return "dumb$$%s" % password

    def verify(self, password, encoded):
        algorithm, hash = encoded.split("$$", 1)
        assert algorithm == "dumb"
        return password == hash

    def safe_summary(self, encoded):
        """ This is an unsafe version """
        return {"algorithm": "dumb", "hash": encoded.split("$", 2)[2]}


PASSWORD_HASHERS = (
    'aa_project.settings.pytest.pytest.SimplePasswordHasher',
)

# Email Token Settings
EMAIL_CHALLENGE_EXPIRATION_IN_SECS = 60 * 5
EMAIL_TOKEN_EXPIRATION_IN_SECS = 60 * 60 * 24 * 28
