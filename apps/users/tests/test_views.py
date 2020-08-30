# pylint: disable=redefined-outer-name
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.urls import reverse

import pytest

from apps.users.views import ProfileUpdateView, ProfileView, UserRegisterView


pytestmark = pytest.mark.django_db

class TestUserRegisterView:
    def test_auth_user_cannot_access(self, factory, auth_user):
        """ Asserts an authenticated user cannot access the
            `registration` view """
        path = reverse('blog:users:register')
        request = factory.get(path)
        request.user = auth_user
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_can_access(self, factory):
        """ Asserts and unauthenticated user can access the
            `registration` view """
        path = reverse('blog:users:register')
        request = factory.get(path)
        request.user = AnonymousUser()
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestProfileView:
    def test_all_users_can_access(self, factory, all_users, li_sec_user):
        """ Asserts the `profile` view is accessible by authenticated
            and unauthenticated users """
        kwargs = {'username': li_sec_user.username}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = factory.get(path)
        request.username = all_users
        response = ProfileView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'


class TestProfileUpdateView:
    def test_auth_user_can_access(self, factory, auth_user):
        """ Asserts the `profile update` view is accessible by an
            authenticated user """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = factory.get(path)
        request.user = auth_user
        response = ProfileUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_cannot_access(self, factory, auth_user):
        """ Asserts the `profile update` view is inaccessible by an
            unauthenticated user """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = ProfileUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should return with an `redirect` status code'
        assert '/login/' in response.url, 'Should redirect to login page'

    def test_another_user_cannot_access(self, factory, auth_user, li_sec_user):
        """ Verify that the `profile update` view is inaccessible by an
            unauthenticated user """
        kwargs = {'username': auth_user.username}
        path = reverse('blog:users:profile_update', kwargs=kwargs)
        request = factory.get(path)
        request.user = li_sec_user
        with pytest.raises(PermissionDenied):
            response = ProfileUpdateView.as_view()(request, **kwargs)
            assert response.status_code == 403, \
                'Should return a `Permission Denied` status code'


@pytest.mark.django_db
@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestAuthViews:
    def test_all_users_can_login(self, factory, all_users):
        """ Asserts the `login` view is publicly accessible """
        path = reverse('blog:users:login')
        request = factory.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_password_reset(self, factory, all_users):
        """ Asserts the `password reset` view is publicly accessible """
        path = reverse('blog:users:password_reset_form')
        request = factory.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_access_password_reset_done(self, factory, all_users):
        """ Asserts the `password reset done` view is publicly accessible """
        path = reverse('blog:users:password_reset_done')
        request = factory.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_all_users_can_access_password_reset_complete(self, factory, all_users):
        """ Asserts the `password reset complete` view is publicly
        accessible """
        path = reverse('blog:users:password_reset_complete')
        request = factory.get(path)
        request.user = all_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'
