import os

from ab_back_end.settings import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BASE_DIR,
                                  DATABASES, DEFAULT_FROM_EMAIL_SES, EMAIL_BACKEND,
                                  EMAIL_HOST_PASSWORD_SES, EMAIL_HOST_SES,
                                  EMAIL_HOST_USER_SES, EMAIL_PORT, EMAIL_USE_TLS,
                                  INSTALLED_APPS, LOGIN_URL, LOGOUT_REDIRECT_URL,
                                  MIDDLEWARE, TEMPLATES)


class TestLoginLogoutUTLs:
    """ Asserts the login, login/logout redirection
        URLS are set up as intended """

    def test_login_url(self):
        assert LOGIN_URL == 'blog:users:login'

    def test_login_redirect_url(self):
        assert LOGOUT_REDIRECT_URL == 'blog:home'

    def test_logout_redirect_url(self):
        assert LOGOUT_REDIRECT_URL == 'blog:home'


class TestThirdPartyAppsAreInstalled:
    """ Asserts that required third party apps are
        correctly integrated within the project. """

    def test_rest_framework_in_installed_apps(self):
        assert 'rest_framework' in INSTALLED_APPS

    def test_guardian_in_installed_apps(self):
        assert 'guardian' in INSTALLED_APPS

    def test_crispy_forms_in_installed_apps(self):
        assert 'crispy_forms' in INSTALLED_APPS

    def test_bootstrap4_in_installed_apps(self):
        assert 'bootstrap4' in INSTALLED_APPS

    def test_storages_in_installed_apps(self):
        assert 'storages' in INSTALLED_APPS

    def test_ckeditor_in_installed_apps(self):
        assert 'ckeditor' in INSTALLED_APPS

    def test_ckeditor_uploader_in_installed_apps(self):
        assert 'ckeditor_uploader' in INSTALLED_APPS

    def test_captcha_in_installed_apps(self):
        assert 'captcha' in INSTALLED_APPS

    def test_google_analytics_in_installed_apps(self):
        assert 'google_analytics' in INSTALLED_APPS

    def test_widget_tweaks_in_installed_apps(self):
        assert 'widget_tweaks' in INSTALLED_APPS


class TestMiddlewareIsConfigured:
    def test_whitenoise_is_in_middleware_config(self):
        assert 'whitenoise.middleware.WhiteNoiseMiddleware' in MIDDLEWARE


class TestTemplatesAreConfigured:
    def test_template_backend_is_configured(self):
        assert TEMPLATES[0]['BACKEND'] == 'django.template.backends.django.DjangoTemplates'

    def test_template_directories_are_present(self):
        temp_dirs = TEMPLATES[0]['DIRS']
        assert os.path.join(BASE_DIR, 'templates') in temp_dirs
        assert os.path.join(BASE_DIR, 'ab_back_end/templates/') in temp_dirs
        assert os.path.join(BASE_DIR, 'ab_back_end/templates/admin/') in temp_dirs
        assert 'pages/templates/pages/' in temp_dirs
        assert 'blog/templates/blog/' in temp_dirs
        assert 'cv/templates/cv/' in temp_dirs
        assert 'users/templates/users/' in temp_dirs
        assert 'users/templates/registration/' in temp_dirs
        assert 'contacts/templates/contacts/' in temp_dirs
        assert 'countdown_letters/templates/countdown_letters/' in temp_dirs
        assert 'countdown_numbers/templates/countdown_numbers/' in temp_dirs
        assert 'text_analysis/templates/text_analysis/' in temp_dirs
        assert 'roulette/templates/roulette/' in temp_dirs
        assert 'scraping/templates/scraping/' in temp_dirs


class TestDatabaseIsSecurelyConfigured:
    def test_secure_database_setup(self):
        assert DATABASES['default']['NAME'] == os.environ['DB_NAME']
        assert DATABASES['default']['USER'] == os.environ['DB_USER']
        assert DATABASES['default']['PASSWORD'] == os.environ['DB_PASS']
        assert DATABASES['default']['HOST'] == os.environ['DB_DOCKER_POSTGRES_SERVICE']
        assert DATABASES['default']['PORT'] == os.environ['DB_PORT']


class TestEmailProviderConfigured:
    def test_test_amazon_ses_setup(self):
        assert EMAIL_BACKEND == 'django_ses.SESBackend'
        assert EMAIL_USE_TLS
        assert EMAIL_HOST_SES == os.environ['EMAIL_HOST_SES']
        assert EMAIL_HOST_USER_SES == os.environ['EMAIL_HOST_USER_SES']
        assert EMAIL_HOST_PASSWORD_SES == os.environ['EMAIL_HOST_PASSWORD_SES']
        assert AWS_ACCESS_KEY_ID == os.environ['AWS_ACCESS_KEY_ID']
        assert AWS_SECRET_ACCESS_KEY == os.environ['AWS_SECRET_ACCESS_KEY']
        assert EMAIL_PORT == 587
        assert DEFAULT_FROM_EMAIL_SES == os.environ['DEFAULT_FROM_EMAIL_SES']