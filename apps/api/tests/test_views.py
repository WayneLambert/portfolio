from django.urls import reverse

import pytest

from apps.api.views import CategoryListAPIView, PostDetailAPIView, PostListAPIView


pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestCategoryListAPIView:
    def test_site_visitor_can_access_category_list_api(self, request, rf, unauth_user):
        """ Asserts a random visitor can access the category list API """
        url = reverse('api:blog_categories')
        request = rf.get(url)
        request.user = unauth_user
        response = CategoryListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_category_list_api(self, request, rf, auth_user):
        """ Asserts an authenticated user can access the category list API """
        url = reverse('api:blog_categories')
        request = rf.get(url)
        request.user = auth_user
        response = CategoryListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'


class TestPostListAPIView:
    def test_site_visitor_can_access_post_list_api(self, request, rf, unauth_user):
        """ Asserts a random visitor can access the post list API """
        url = reverse('api:posts')
        request = rf.get(url)
        request.user = unauth_user
        response = PostListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_post_list_api(self, request, rf, auth_user):
        """ Asserts an authenticated user can access the post list API """
        url = reverse('api:posts')
        request = rf.get(url)
        request.user = auth_user
        response = PostListAPIView.as_view()(request)
        assert response.status_code == 200, 'Should return an OK status code'


class TestPostDetailAPIView:
    def test_site_visitor_can_access_post_detail_api(self, request, rf, unauth_user, pub_post):
        """ Asserts a random visitor can access the post detail API """
        url = reverse('api:post_detail', kwargs={'pk': pub_post.id})
        request = rf.get(url)
        request.user = unauth_user
        response = PostDetailAPIView.as_view()(request, pk=pub_post.id)
        assert response.status_code == 200, 'Should return an OK status code'

    def test_auth_user_can_access_post_detail_api(self, request, rf, auth_user, pub_post):
        """ Asserts an authenticated user can access the post detail API """
        url = reverse('api:post_detail', kwargs={'pk': pub_post.id})
        request = rf.get(url)
        request.user = auth_user
        response = PostDetailAPIView.as_view()(request, pk=pub_post.id)
        assert response.status_code == 200, 'Should return an OK status code'
