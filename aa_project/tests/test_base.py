import os

import pytest

from aa_project.settings import base


class TestLoginLogoutUTLs:
    """ Asserts redirection URLS are set up as intended """

    def test_login_url(self):
        assert base.LOGIN_URL == 'blog:users:login'

    def test_login_redirect_url(self):
        assert base.LOGIN_REDIRECT_URL == 'blog:home'

    def test_logout_redirect_url(self):
        assert base.LOGOUT_REDIRECT_URL == 'blog:home'


class TestThirdPartyAppsAreInstalled:
    """ Asserts that required third party apps are
        correctly integrated within the project. """

    def test_whitenoise_in_installed_apps(self):
        assert 'whitenoise.runserver_nostatic' in base.INSTALLED_APPS

    def test_rest_framework_in_installed_apps(self):
        assert 'rest_framework' in base.INSTALLED_APPS

    def test_guardian_in_installed_apps(self):
        assert 'guardian' in base.INSTALLED_APPS

    def test_crispy_forms_in_installed_apps(self):
        assert 'crispy_forms' in base.INSTALLED_APPS

    def test_crispy_bootstrap4_in_installed_apps(self):
        assert 'crispy_bootstrap4' in base.INSTALLED_APPS

    def test_storages_in_installed_apps(self):
        assert 'storages' in base.INSTALLED_APPS

    def test_django_recaptcha_in_installed_apps(self):
        assert 'django_recaptcha' in base.INSTALLED_APPS

    def test_widget_tweaks_in_installed_apps(self):
        assert 'widget_tweaks' in base.INSTALLED_APPS

    def test_tinymce_in_installed_apps(self):
        assert 'tinymce' in base.INSTALLED_APPS


class TestMiddlewareIsConfigured:
    def test_whitenoise_is_in_middleware_config(self):
        assert 'whitenoise.middleware.WhiteNoiseMiddleware' in base.MIDDLEWARE


class TestTemplatesAreConfigured:
    def test_template_backend_is_configured(self):
        assert base.TEMPLATES[0]['BACKEND'] == 'django.template.backends.django.DjangoTemplates'

    def test_template_directories_are_present(self):
        temp_dirs = base.TEMPLATES[0]['DIRS']
        assert os.path.join(base.BASE_DIR, 'templates') in temp_dirs
        assert os.path.join(base.BASE_DIR, 'aa_project/templates/') in temp_dirs
        assert os.path.join(base.BASE_DIR, 'aa_project/templates/admin/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'blog/templates/blog/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'cv/templates/cv/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'contacts/templates/contacts/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'countdown_letters/templates/countdown_letters/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'countdown_numbers/templates/countdown_numbers/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'pages/templates/pages/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'roulette/templates/roulette/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'scraping/templates/scraping/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'text_analysis/templates/text_analysis/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'users/templates/users/') in temp_dirs
        assert os.path.join(base.APPS_DIR, 'users/templates/registration/') in temp_dirs


@pytest.mark.skipif('GITHUB_RUN_ID' in os.environ, reason='Different DB credentials in GitHub Actions')
class TestDatabaseIsSecurelyConfigured:
    def test_secure_database_setup(self):
        assert base.DATABASES['default']['NAME'] == os.environ['DB_NAME']
        assert base.DATABASES['default']['USER'] == os.environ['DB_USER']
        assert base.DATABASES['default']['PASSWORD'] == os.environ['DB_PASS']
        assert base.DATABASES['default']['HOST'] == os.environ['DB_DOCKER_POSTGRES_SERVICE']
        assert base.DATABASES['default']['PORT'] == os.environ['DB_PORT']


class TestEmailProviderConfigured:
    def test_amazon_ses_setup(self):
        assert base.EMAIL_BACKEND == 'django_ses.SESBackend'
        assert base.EMAIL_USE_TLS
        assert base.EMAIL_HOST_SES == os.environ['EMAIL_HOST_SES']
        assert base.EMAIL_HOST_USER_SES == os.environ['EMAIL_HOST_USER_SES']
        assert base.EMAIL_HOST_PASSWORD_SES == os.environ['EMAIL_HOST_PASSWORD_SES']
        assert base.AWS_ACCESS_KEY_ID == os.environ['AWS_ACCESS_KEY_ID']
        assert base.AWS_SECRET_ACCESS_KEY == os.environ['AWS_SECRET_ACCESS_KEY']
        assert base.EMAIL_PORT == 587
        assert base.DEFAULT_FROM_EMAIL_SES == os.environ['DEFAULT_FROM_EMAIL_SES']
