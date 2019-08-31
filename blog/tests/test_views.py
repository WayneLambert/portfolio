# pylint: disable=redefined-outer-name
import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
import blog.views as blog_views
pytestmark = pytest.mark.django_db  # Request database access


def test_home(factory):
    """ Determines whether any user can access complete list of posts """
    path = reverse('blog-django')
    request = factory.get(path)
    response = blog_views.home(request)
    assert response.status_code == 200, 'Should be callable by anyone'
    assert response.charset == 'utf-8', 'Should be encoded with the utf-8 characterset'


class TestPostListView:
    """ Determines whether any user can access complete list of posts """
    def test_post_list_view(self, factory):
        path = reverse('blog-django')
        request = factory.get(path)
        response = blog_views.PostListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestUserPostListView:
    """
    Determines whether any user can access list of
    filtered posts authored by username parameter
    """
    def test_user_post_list_view(self, factory, user):
        kwargs = {'username': user.username}
        path = reverse('user-posts', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.UserPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestCategoryPostListView:
    """
    Determines whether any user can access list of
    filtered posts belonging to a given category
    """
    def test_category_post_list_view(self, factory, category):
        kwargs = {'slug': category.slug}
        path = reverse('category-posts', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.CategoryPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestPostDetailView:
    """ Determines whether any user can access a single post detail view """

    def test_post_detail_view(self, factory, post):
        kwargs = {'slug': post.slug}
        path = reverse('post-detail', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.PostDetailView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestPostCreateView:
    def test_post_create_view_logged_in(self, factory, post, user):
        """
        Asserts logged in user can access the update view of a single post
        """
        kwargs = {'slug': post.slug}
        path = reverse('post-update', kwargs=kwargs)
        request = factory.get(path)
        request.user = user
        response = blog_views.PostCreateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by logged in user'

    def test_post_create_view_logged_out(self, factory, post):
        """
        Asserts logged out user cannot access the update view of a single post
        """
        kwargs = {'slug': post.slug}
        path = reverse('post-update', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostCreateView.as_view()(request, **kwargs)
        assert response.status_code != 200, 'Should not be callable by an anonymous out user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'
