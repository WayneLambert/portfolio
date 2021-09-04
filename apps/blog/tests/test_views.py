from django.urls import reverse

import pytest

import apps.blog.views as blog_views


pytestmark = pytest.mark.django_db(reset_sequences=True)


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestHomeView:
    def test_all_users_can_access(self, rf, all_users):
        """
        Asserts authenticated and unauthenticated user can access
        complete list of posts
        """
        path = reverse('blog:home')
        request = rf.get(path)
        request.user = all_users
        response = blog_views.HomeView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestAuthorPostListView:
    def test_all_users_can_access(self, rf, pub_posts, all_users):
        """
        Asserts authenticated and unauthenticated user can access
        list of posts written by another author
        """
        author_username = pub_posts[0].author.get_username()
        kwargs = {'username': author_username}
        path = reverse('blog:author_posts', kwargs=kwargs)
        request = rf.get(path)
        request.user = all_users
        response = blog_views.AuthorPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestCategoryPostListView:
    def test_all_users_can_access(self, rf, category, all_users):
        """
        Asserts authenticated and unauthenticated user can access list
        of posts in a given category
        """
        kwargs = {'slug': category.slug}
        path = reverse('blog:category_posts', kwargs=kwargs)
        request = rf.get(path)
        request.user = all_users
        response = blog_views.CategoryPostListView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestPostDetailView:
    def test_all_users_can_access(self, rf, pub_post, all_users):
        """
        Asserts an authenticated and unauthenticated user can access a
        single post detail view
        """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_detail', kwargs=kwargs)
        request = rf.get(path)
        request.user = all_users
        response = blog_views.PostDetailView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'


class TestPostCreateView:
    path = reverse('blog:post_create')

    def test_auth_user_can_access(self, rf, auth_user):
        """ Asserts authenticated user can access the view """
        request = rf.get(self.path)
        request.user = auth_user
        response = blog_views.PostCreateView.as_view()(request)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_cannot_access(self, rf, unauth_user):
        """ Asserts unauthenticated user cannot access the view """
        request = rf.get(self.path)
        request.user = unauth_user
        response = blog_views.PostCreateView.as_view()(request)
        assert response.status_code == 302, 'Should be redirected to the `login` page'
        assert 'login/?next=' and '/new' in response.url, 'Should redirect to login screen'


class TestPostUpdateView:
    def test_author_can_access(self, rf, pub_post):
        """ Asserts post's author can access the update view of a post """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = rf.get(path)
        request.user = pub_post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return an `OK` status code'

    def test_unauth_user_cannot_access(self, rf, unauth_user, pub_post):
        """ Asserts unauthenticated user cannot access post update view """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = rf.get(path)
        request.user = unauth_user
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should return `OK` status code by logged in author'
        assert '/login/?next=' in response.url, 'Should redirect to login page'
        assert (
            f'{pub_post.slug}/update' in response.url
        ), 'Should redirect to login page'

    def test_author_can_update(self, rf, pub_post):
        """ Asserts author can update the post """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_update', kwargs=kwargs)
        request = rf.post(path)
        request.user = pub_post.author
        response = blog_views.PostUpdateView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should redirect user to detail page upon update'


class TestPostDeleteView:
    def test_author_can_delete(self, rf, pub_post):
        """ Asserts author can access the delete view of a single post """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_delete', kwargs=kwargs)
        request = rf.get(path)
        request.user = pub_post.author
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 200, 'Should return `OK` status code by author'

    def test_unauth_user_cannot_delete(self, rf, unauth_user, pub_post):
        """ Asserts unauthenticated user cannot delete the post """
        kwargs = {'slug': pub_post.slug}
        path = reverse('blog:post_delete', kwargs=kwargs)
        request = rf.post(path)
        request.user = unauth_user
        response = blog_views.PostDeleteView.as_view()(request, **kwargs)
        assert response.status_code == 302, 'Should redirect user'
        assert '/blog/' in response.url, '`blog` should appear in URL following redirect'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestSearchView:
    def test_all_users_can_access(self, rf, all_users):
        """
        Asserts authenticated and unauthenticated users can retrieve
        the search page
        """
        path = reverse('blog:search')
        request = rf.get(path)
        request.user = all_users
        response = blog_views.SearchView.as_view()(request)
        assert response.status_code == 200, 'Search results should be returned'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestSearchResultsView:
    def test_all_users_can_access_searches(self, rf, pub_posts, search_terms, all_users):
        """
        Asserts authenticated and unauthenticated users can retrieve
        search results of qualified post(s)
        """
        path = f"{reverse('blog:search_results')}{'?q='}{search_terms}"
        request = rf.get(path)
        request.user = all_users
        response = blog_views.SearchResultsView.as_view()(request)
        assert response.status_code == 200, 'Search results should be returned'


@pytest.mark.parametrize(argnames='all_users',
    argvalues=[pytest.param('auth_user'), pytest.param('unauth_user')], indirect=True)
class TestContentsListView:
    def test_all_users_can_access(self, rf, pub_posts, all_users):
        """ Asserts unauthenticated users can access `contents` page """
        path = reverse('blog:contents')
        request = rf.get(path)
        request.user = all_users
        response = blog_views.ContentsListView.as_view()(request)
        assert response.status_code == 200, 'Should return `OK` status code by unauth user'
