# pylint: disable=redefined-outer-name
import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

import blog.views as blog_views
from ab_back_end.tests.helpers import lilo_users, user_types

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestHomeView:
    def test_home(self, request, factory, lilo_users):
        """ Asserts any user can access complete list of posts """
        path = reverse('blog:home')
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.HomeView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'
        assert response.charset == 'utf-8', 'Should be encoded with the utf-8 characterset'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestUserPostListView:
    def test_user_post_list_view(self, request, factory, random_user, lilo_users):
        """ Asserts any user can access list of posts authored by username """
        kwargs = {'username': random_user.username}
        path = reverse('blog:user_posts', kwargs=kwargs)
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.UserPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestCategoryPostListView:
    def test_category_post_list_view(self, request, factory, category, lilo_users):
        """ Asserts any user can access list of posts in a given category """
        kwargs = {'slug': category.slug}
        path = reverse('blog:category_posts', kwargs=kwargs)
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.CategoryPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestPostDetailView:
    def test_post_detail_view(self, request, factory, post, lilo_users):
        """ Asserts any user can access a single post detail view """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_detail', kwargs=kwargs)
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.PostDetailView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by anyone'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestPostCreateView:
    def test_post_create_view(self, request, factory, lilo_users):
        """ Asserts logged in user can create a post """
        path = reverse('blog:post_create')
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.PostCreateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by logged in user'


class TestPostUpdateView:
    def test_post_update_view_logged_in_GET(self, request, factory, post):
        """ Asserts author can access the update view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = factory.get(path)
        request.user = post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by logged in author'

    def test_post_update_view_logged_in_POST(self, request, factory, post):
        """ Asserts author can update the post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = factory.post(path)
        request.user = post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should redirect user to detail page upon update'

    def test_post_update_view_logged_out(self, request, factory, post):
        """ Asserts logged out user cannot access the update view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code != 200, 'Should not be callable by an anonymous user'
        assert response.status_code == 302, 'Should redirect user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'


class TestPostDeleteView:
    def test_post_delete_view_logged_in_GET(self, request, factory, post):
        """ Asserts author can access the delete view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_delete', kwargs=kwargs)
        request = factory.get(path)
        request.user = post.author
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should be callable by author'


    def test_post_delete_view_logged_in_POST(self, request, factory, post):
        """ Asserts author can delete the post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_delete', kwargs=kwargs)
        request = factory.post(path)
        request.user = post.author
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should redirect author to blog home page on deletion'
        assert '/blog/' in response.url, '`blog` should appear in url following redirect'


    def test_post_delete_view_logged_out(self, request, factory, post):
        """ Asserts logged out user cannot access the delete view of a single post """
        kwargs = {'slug': post.slug}
        path = reverse('blog:post_delete', kwargs=kwargs)
        request = factory.get(path)
        request.user = AnonymousUser()
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code != 200, 'Should not be callable by an anonymous user'
        assert response.status_code == 302, 'Should redirect user'
        assert 'login/?next=' in response.url, 'Should redirect anonymous user to login screen'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestSearchResultsView:
    def test_search_results_view_logged_in(self, request, factory, search_terms, lilo_users):
        """ Asserts logged in/out users can retrieve search results of qualified post(s) """
        for index, _ in enumerate(search_terms):
            path = f"({reverse('blog:search_results')}{'?q='}{search_terms[index]})"
            request = factory.get(path)
            request.user = lilo_users
            response = blog_views.SearchResultsView.as_view()(request)
            assert response.status_code == 200, 'Search results should be returned by any user'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestContentsListView:
    def test_contents_list_view(self, request, factory, lilo_users):
        """ Asserts logged in/out users can access `contents` page """
        path = reverse('blog:contents')
        request = factory.get(path)
        request.user = lilo_users
        response = blog_views.ContentsListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by logged in/out user'
