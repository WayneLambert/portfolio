import pytest
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from ab_back_end.tests.helpers import lilo_users, user_types
from users.views import ProfileView, UserRegisterView, profile_update

pytestmark = pytest.mark.django_db

class TestUserRegisterView:
    def test_auth_user_cannot_register(self, request, factory, li_user):
        """ Asserts and authenticated user cannot access the `registration` view """
        path = reverse('blog:users:register')
        request = factory.get(path)
        request.user = li_user
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'

    def test_unauth_user_can_register(self, request, factory):
        """ Asserts and unauthenticated user can access the `registration` view """
        path = reverse('blog:users:register')
        request = factory.get(path)
        request.user = AnonymousUser()
        response = UserRegisterView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'


class TestProfileView:
    def test_profile(self, request, factory, li_prim_user):
        """ Verify that the `profile` view is publicly accessible """
        kwargs={'username': li_prim_user.username}
        path = reverse('blog:users:profile', kwargs=kwargs)
        request = factory.get(path)
        request.username = lilo_users
        response = ProfileView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return with an `OK` status code'


def test_profile_update_view_inaccessible_unauth_user(request, factory, li_prim_user):
    """ Verify that the `profile update` view is inaccessible by an unauthenticated user """
    path = reverse('blog:users:profile_update', kwargs={'username': li_prim_user.username})
    request = factory.get(path)
    request.user = AnonymousUser()
    response = profile_update(request, kwargs=li_prim_user.username)
    assert response.status_code == 302, 'Should return with an `redirect` status code'
    assert '/login/' in response.url, 'Should redirect to login page'


def test_profile_update_view_inaccessible_another_user(request, factory, li_prim_user, li_sec_user):
    """ Verify that the `profile update` view is inaccessible by an unauthenticated user """
    path = reverse('blog:users:profile_update', kwargs={'username': li_prim_user.username})
    request = factory.get(path)
    request.user = li_sec_user
    response = profile_update(request, kwargs=li_prim_user.username)
    assert response.status_code == 404, 'Should return with a `page not found` status code'


@pytest.mark.django_db
@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestAuthViews:
    def test_login(self, factory, lilo_users):
        """ Verify that the `login` view is publicly accessible """
        path = reverse('blog:users:login')
        request = factory.get(path)
        request.user = lilo_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'

    def test_password_reset(self, factory, lilo_users):
        """ Verify that the `password reset` view is publicly accessible """
        path = reverse('blog:users:password_reset_form')
        request = factory.get(path)
        request.user = lilo_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'

    def test_password_reset_done(self, factory, lilo_users):
        """ Verify that the `password reset done` view is publicly accessible """
        path = reverse('blog:users:password_reset_done')
        request = factory.get(path)
        request.user = lilo_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'

    def test_password_reset_complete(self, factory, lilo_users):
        """ Verify that the `password reset complete` view is publicly accessible """
        path = reverse('blog:users:password_reset_complete')
        request = factory.get(path)
        request.user = lilo_users
        response = auth_views.LoginView.as_view()(request)
        assert response.status_code == 200, 'Should return with an `OK` status code'
