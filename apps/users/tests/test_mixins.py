from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView

import helpers as apps_helpers

from users.mixins import DeviceAuthUserMixin, EmailAuthUserMixin, TwoFactorAuthUserMixin


class TestDeviceAuthUserMixin:

    class ExampleDeviceAuthView(DeviceAuthUserMixin, TemplateView):
        template_name = 'random_template.html'

    def test_device_auth_user_passes_test_func(self, rf, device_auth_user):
        request = rf.get('/any-random-url/')
        request.user = device_auth_user
        self.ExampleDeviceAuthView.as_view()(request)
        assert request.user.profile.is_two_factor_auth_by_token

    def test_email_auth_user_fails_test_func(self, rf, email_auth_user):
        request = rf.get('/any-random-url/')
        request.user = email_auth_user
        self.ExampleDeviceAuthView.as_view()(request)
        assert not request.user.profile.is_two_factor_auth_by_token

    def test_handle_no_permission(self, rf, auth_user):
        request = rf.get('/any-random-url/')
        request.user = auth_user
        response = self.ExampleDeviceAuthView.as_view()(request)
        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302, 'Should redirect the user'
        assert '/users/login/' in response.url, 'Should return the user to the login page'


class TestEmailAuthUserMixin:

    class ExampleEmailAuthView(EmailAuthUserMixin, TemplateView):
        template_name = 'random_template.html'

    def test_device_auth_user_fails_test_func(self, rf, device_auth_user):
        request = rf.get('/any-random-url/')
        request.user = device_auth_user
        self.ExampleEmailAuthView.as_view()(request)
        assert not request.user.profile.is_two_factor_auth_by_email

    def test_email_auth_user_passes_test_func(self, rf, email_auth_user):
        request = rf.get('/any-random-url/')
        request.user = email_auth_user
        self.ExampleEmailAuthView.as_view()(request)
        assert request.user.profile.is_two_factor_auth_by_email

    def test_handle_no_permission(self, rf, auth_user):
        request = rf.get('/any-random-url/')
        request.user = auth_user
        response = self.ExampleEmailAuthView.as_view()(request)
        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302, 'Should redirect the user'
        assert '/users/login/' in response.url, 'Should return the user to the login page'


class TestTwoFactorAuthUserMixin:

    class ExampleTwoFactorAuthView(TwoFactorAuthUserMixin, TemplateView):
        template_name = 'random_template.html'

    def test_device_auth_user_passes_test_func(self, rf, device_auth_user):
        request = rf.get('/any-random-url/')
        request.user = device_auth_user
        self.ExampleTwoFactorAuthView.as_view()(request)
        assert request.user.profile.is_two_factor_authenticated

    def test_email_auth_user_passes_test_func(self, rf, email_auth_user):
        request = rf.get('/any-random-url/')
        request.user = email_auth_user
        self.ExampleTwoFactorAuthView.as_view()(request)
        assert request.user.profile.is_two_factor_authenticated

    def test_handle_no_permission(self, rf, auth_user):
        request = rf.get('/any-random-url/')
        request.user = auth_user
        apps_helpers.add_middlewares(request)
        response = self.ExampleTwoFactorAuthView.as_view()(request)
        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302, 'Should redirect the user'
        assert '/users/login/' in response.url, 'Should return the user to the login page'
