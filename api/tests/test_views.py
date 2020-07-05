import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from api.tests.factories import UserFactory
from api.views import CategoryListAPIView, PostDetailAPIView, PostListAPIView

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestCategoryListAPIView:
    def test_site_visitor_can_access_category_list_api(self, request, factory):
        """ Asserts a random visitor can access the category list API """
        url = reverse('api:blog_categories')
        request = factory.get(url)
        request.user = AnonymousUser()
        response = CategoryListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_category_list_api(self, request, factory):
        """ Asserts an authenticated user can access the category list API """
        url = reverse('api:blog_categories')
        request = factory.get(url)
        request.user = UserFactory()
        response = CategoryListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_site_visitor_can_access_post_list_api(self, request, factory):
        """ Asserts a random visitor can access the post list API """
        url = reverse('api:posts')
        request = factory.get(url)
        request.user = AnonymousUser()
        response = PostListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_post_list_api(self, request, factory):
        """ Asserts an authenticated user can access the post list API """
        url = reverse('api:posts')
        request = factory.get(url)
        request.user = UserFactory()
        response = PostListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_site_visitor_can_access_post_detail_api(self, request, factory, post):
        """ Asserts a random visitor can access the post detail API """
        url = reverse('api:post_detail', kwargs={'pk': post.id})
        request.user = AnonymousUser()
        request = factory.get(url)
        response = PostDetailAPIView.as_view()(request, pk=post.id)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_post_detail_api(self, request, factory, post):
        """ Asserts an authenticated user can access the post detail API """
        url = reverse('api:post_detail', kwargs={'pk': post.id})
        request.user = UserFactory()
        request = factory.get(url)
        response = PostDetailAPIView.as_view()(request, pk=post.id)
        assert response.status_code == 200, 'Should return an OK status code'
