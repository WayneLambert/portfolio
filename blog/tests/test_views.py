# pylint: disable=redefined-outer-name
from urllib.parse import urlparse
import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
import blog.views as blog_views
pytestmark = pytest.mark.django_db  # Request database access


def test_home(factory):
    """ Asserts any user can access complete list of posts """
    path = reverse('blog-django')
    request = factory.get(path)
    response = blog_views.home(request)
    assert response.status_code == 200, 'Should be callable by anyone'
    assert response.charset == 'utf-8', 'Should be encoded with the utf-8 characterset'


class TestPostListView:
    def test_post_list_view(self, factory):
        """ Asserts any user can access complete list of posts """
        path = reverse('blog-django')
        request = factory.get(path)
        response = blog_views.PostListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestUserPostListView:
    def test_user_post_list_view(self, factory, user):
        """ Asserts any user can access list of posts authored by username """
        kwargs = {'username': user.username}
        path = reverse('user-posts', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.UserPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestCategoryPostListView:
    def test_category_post_list_view(self, factory, category):
        """ Asserts any user can access list of posts in a given category """
        kwargs = {'slug': category.slug}
        path = reverse('category-posts', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.CategoryPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestPostDetailView:
    def test_post_detail_view(self, factory, post):
        """ Asserts any user can access a single post detail view """
        kwargs = {'slug': post.slug}
        path = reverse('post-detail', kwargs=kwargs)
        request = factory.get(path)
        response = blog_views.PostDetailView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


class TestPostCreateView:
    def test_post_create_view_logged_in(self, factory, user):
        """ Asserts logged in user can create a post """
        path = reverse('post-create')
        request = factory.get(path)
        request.user = user
        response = blog_views.PostCreateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by logged in user'

    def test_post_create_view_logged_out(self, factory):
        """ Asserts logged out user cannot create a post """
        path = reverse('post-create')
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostCreateView.as_view()(request)
        assert response.status_code != 200, 'Should not be callable by an anonymous user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'


class TestPostUpdateView:
    def test_post_update_view_logged_in_GET(self, factory, post):
        """ Asserts logged in user can access the update view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('post-update', kwargs=kwargs)
        request = factory.get(path)
        request.user = post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by logged in user'

    def test_post_update_view_logged_in_POST(self, factory, post):
        """ Asserts logged in user can update the post """
        kwargs = {'slug': post.slug}
        path = reverse('post-detail', kwargs=kwargs)
        request = factory.post(path)
        request.user = post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should redirect user upon update'

    def test_post_update_view_logged_out(self, factory, post):
        """ Asserts logged out user cannot access the update view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('post-update', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code != 200, 'Should not be callable by an anonymous user'
        assert response.status_code == 302, 'Should redirect user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'


class TestPostDeleteView:
    def test_post_delete_view_logged_in_GET(self, factory, post):
        """ Asserts logged in user can access the delete view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('post-delete', kwargs=kwargs)
        request = factory.get(path)
        request.user = post.author
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by logged in user'

    def test_post_delete_view_logged_in_POST(self, factory, post):
        """ Asserts logged in user can delete the post """
        kwargs = {'slug': post.slug}
        path = reverse('post-delete', kwargs=kwargs)
        request = factory.post(path)
        request.user = post.author
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should redirect user to blog home page on deletion'
        assert '/blog/' in response.url, '`blog` should appear in url following redirect'

    def test_post_delete_view_logged_out(self, factory, post):
        """ Asserts logged out user cannot access the delete view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('post-delete', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code != 200, 'Should not be callable by an anonymous user'
        assert response.status_code == 302, 'Should redirect user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'


class TestSearchResultsView:
    def test_search_results_view_logged_in(self, factory, search_terms, user):
        """ Asserts logged in user can retrieve search results of qualified post(s) """
        for index, item in enumerate(search_terms):
            path = f"({reverse('search-results')}{'?q='}{search_terms[index]})"
            request = factory.get(path)
            request.user = user
            response = blog_views.SearchResultsView.as_view()(request)
            assert response.status_code == 200, 'Search results should be returned by logged in user'

    def test_search_results_view_logged_out(self, factory, search_terms):
        """ Asserts anonymous user can retrieve search results of qualified post(s) """
        for index, item in enumerate(search_terms):
            path = f"({reverse('search-results')}{'?q='}{search_terms[index]})"
            request = factory.get(path)
            request.user = AnonymousUser()
            response = blog_views.SearchResultsView.as_view()(request)
            assert response.status_code == 200, 'Search results should be returned by anyone'
