from django.conf import settings
from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import resolve_url
from django.urls import reverse

import pytest

import apps.helpers as apps_helpers

from apps.users.models import Profile
from apps.users.views import (ProfileUpdateView, ProfileView, UserLoginView,
                              UserRegisterView,)


pytestmark = pytest.mark.django_db(reset_sequences=True)

class TestUserRegisterView:

    path = reverse('blog:users:register')

    def test_auth_user_cannot_access(self, rf, auth_user):
        """ Asserts authenticated user can't access `registration` iew """
        request = rf.get(self.path)
        request.user = auth_user
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_can_access(self, rf, unauth_user):
        """ Asserts unauthenticated user can access `registration` view """
        request = rf.get(self.path)
        request.user = unauth_user
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_form_valid(self, rf, django_user_model, sample_user_data):
        """
        Asserts that a form with valid data is considered valid and
        redirects the user accordingly
        """
        django_user_model.objects.create(username='wayne-lambert', id=2)
        kwargs = sample_user_data
        request = rf.post(self.path, kwargs)
        apps_helpers.add_middlewares(request)
        response = UserRegisterView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should be redirected'
        assert '/blog/' in response.url, 'Should redirect to `blog` home screen'
        assert Profile.objects.count() == 2, 'Should have 2 objects in the database'


class TestProfileView:

    @pytest.mark.django_db(reset_sequences=True)
    def test_unauth_user_is_redirected_to_login(self, rf, unauth_user):
        """ Asserts an unauth user cannot access a non-existent `profile` """
        kwargs = {'username': 'inexistent-user'}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        apps_helpers.add_middlewares(request)
        request.user = unauth_user
        response = ProfileView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should be redirected'
        assert resolve_url(settings.LOGIN_URL) in response.url

    def test_auth_user_is_redirected_to_login(self, rf, auth_user):
        """
        Asserts an authenticated user cannot access an inexistent
        profile and is redirected to the site's login page
        """
        kwargs = {'username': 'inexistent-user'}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        apps_helpers.add_middlewares(request)
        request.user = auth_user
        response = ProfileView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should be redirected'
        assert resolve_url(settings.LOGIN_URL) in response.url

    def test_device_auth_user_cannot_access_inexistent_profile(self, rf, device_auth_user):
        """
        Asserts a user that has fully set up two-factor authentication
        using their device cannot access a non-existent `profile`,
        therefore they're returned a 404 error
        """
        kwargs = {'username': 'inexistent-user'}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        request.user = device_auth_user
        assert request.user.profile.is_two_factor_auth_by_token
        with pytest.raises(Http404):
            ProfileView.as_view()(request, **kwargs)

    def test_email_auth_user_cannot_access_inexistent_profile(self, rf, email_auth_user):
        """
        Asserts a user that has fully set up two-factor authentication
        using their email cannot access a non-existent `profile`,
        therefore they're returned a 404 error
        """
        kwargs = {'username': 'inexistent-user'}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        request.user = email_auth_user
        assert request.user.profile.is_two_factor_auth_by_email
        with pytest.raises(Http404):
            ProfileView.as_view()(request, **kwargs)


class TestProfileUpdateView:
    def test_auth_user_can_access(self, rf, auth_user):
        """
        Asserts the `profile update` view is accessible by an
        authenticated user
        """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = rf.get(path)
        request.user = auth_user
        response = ProfileUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_cannot_access(self, rf, auth_user, unauth_user):
        """
        Asserts `profile update` view inaccessible by unauthenticated user
        """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = rf.get(path)
        request.user = unauth_user
        apps_helpers.add_middlewares(request)
        response = ProfileUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should return with an `redirect` status code'
        assert '/login/' in response.url, 'Should redirect to login page'

    def test_another_user_cannot_access(self, rf, auth_user, li_sec_user):
        """
        Asserts `profile update` view inaccessible by unauthenticated user
        """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = rf.get(path)
        request.user = li_sec_user
        apps_helpers.add_middlewares(request)
        response = ProfileUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Mixin should yield permanent redirect'
        assert resolve_url(settings.LOGIN_URL) in response.url, 'Should redirect to login page'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestAuthViews:

    def test_all_users_can_login(self, rf, all_users):
        """ Asserts the `login` view is publicly accessible """
        path = reverse('blog:users:login')
        request = rf.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_password_reset(self, rf, all_users):
        """ Asserts the `password reset` view is publicly accessible """
        path = reverse('blog:users:password_reset_form')
        request = rf.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_access_password_reset_done(self, rf, all_users):
        """
        Asserts the `password reset done` view is publicly accessible
        """
        path = reverse('blog:users:password_reset_done')
        request = rf.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_access_password_reset_complete(self, rf, all_users):
        """
        Asserts `password reset complete` view is publicly accessible
        """
        path = reverse('blog:users:password_reset_complete')
        request = rf.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'
