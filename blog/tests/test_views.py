# pylint: disable=redefined-outer-name
import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
import blog.views as blog_views
pytestmark = pytest.mark.django_db

@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def post(db):
    return mixer.blend('blog.Post')

@pytest.fixture
def user(db):
    return mixer.blend('auth.User')


def test_home(factory):
    path = reverse('blog-django')
    request = factory.get(path)
    response = blog_views.home(request)
    assert response.status_code == 200, 'Should be callable by anyone'
    assert response.charset == 'utf-8', 'Should be encoded with the utf-8 characterset'


class TestPostListView:
    def test_post_list_view(self, factory):
        path = reverse('blog-django')
        request = factory.get(path)
        response = blog_views.PostListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestUserPostListView:
    def test_user_post_list_view(self, factory, user):
        path = reverse('user-posts', {'username': user})
        request = factory.get(path)
        response = blog_views.UserPostListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

