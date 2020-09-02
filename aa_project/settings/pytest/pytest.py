# pylint: disable=unused-import
import os

from django.contrib.auth.hashers import BasePasswordHasher

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

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

PYTEST_TEST_PASSWORD = os.environ['PYTEST_TEST_PASSWORD']
