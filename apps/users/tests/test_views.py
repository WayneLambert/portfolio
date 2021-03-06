from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse

import pytest

import apps.helpers as apps_helpers

from apps.users.models import Profile
from apps.users.views import ProfileUpdateView, ProfileView, UserRegisterView


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

    @pytest.mark.django_db(reset_sequences=True)
    def test_form_valid(self, rf, django_user_model, sample_user_data):
        """
        Asserts that a form with valid data is considered valid and
        redirects the user accordingly
        """
        django_user_model.objects.create(username='wayne-lambert', id=2)
        kwargs = sample_user_data
        request = rf.post(self.path, kwargs)
        apps_helpers.add_session_and_messages_middlewares(request)
        response = UserRegisterView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should be redirected'
        assert '/blog/' in response.url, 'Should redirect to `blog` home screen'
        assert Profile.objects.count() == 2, 'Should have 2 objects in the database'

    def test_form_invalid(self, rf, django_user_model, sample_user_data):
        """
        Asserts that a found second instance of the same username
        within the database returns `True`
        """
        django_user_model.objects.create(username='wayne-lambert')
        assert Profile.objects.count() == 2, 'Should have 2 objects in the database'
        kwargs = sample_user_data
        request = rf.post(self.path, kwargs)
        apps_helpers.add_session_and_messages_middlewares(request)
        response = UserRegisterView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should be redirected'
        assert '/register/' in response.url, 'Should redirect to `register` screen'
        assert Profile.objects.count() == 2, 'Should still have 2 objects in the database'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestProfileView:
    def test_all_users_can_access(self, rf, all_users, li_sec_user):
        """
        Asserts the `profile` view is accessible by authenticated
        and unauthenticated users
        """
        kwargs = {'username': li_sec_user.username}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        request.username = all_users
        response = ProfileView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_inexistent_profile(self, rf, all_users):
        """
        Asserts an attempt to access a non-existent `profile` view
        returns a 404 error
        """
        kwargs = {'username': 'inexistent-user'}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = rf.get(path)
        request.username = all_users
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
        with pytest.raises(PermissionDenied):
            response = ProfileUpdateView.as_view()(request, **kwargs)
            assert response.status_code == 403, 'Should return a `Permission Denied` status code'


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
