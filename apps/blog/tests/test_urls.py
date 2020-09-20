from django.urls import reverse

from apps.blog.views import (AuthorPostListView, CategoryPostListView, ContentsListView,
                             HomeView, IndexListView, PostCreateView, PostDeleteView,
                             PostDetailView, PostUpdateView, SearchResultsView,
                             SearchView,)


class TestUrls:
    def test_blog_home(self):
        """ Verify that the `home` url invokes intended view """
        path = reverse('blog:home')
        assert path, HomeView.as_view().__name__

    def test_author_posts(self):
        """ Verify that the `author_posts` url invokes intended view """
        path = reverse('blog:author_posts', kwargs={'username': 'test-username'})
        assert path, AuthorPostListView.as_view().__name__

    def test_category_posts(self):
        """ Verify that the `category_posts` url invokes intended view """
        path = reverse('blog:category_posts', kwargs={'slug': 'test-category-slug'})
        assert path, CategoryPostListView.as_view().__name__

    def test_post_create(self):
        """ Verify that the `post_create` url invokes intended view """
        path = reverse('blog:post_create')
        assert path, PostCreateView.as_view().__name__

    def test_post_detail(self):
        """ Verify that the `post_detail` url invokes intended view """
        path = reverse('blog:post_detail', kwargs={'slug': 'test-post-slug'})
        assert path, PostDetailView.as_view().__name__

    def test_post_update(self):
        """ Verify that the `post_update` url invokes intended view """
        path = reverse('blog:post_update', kwargs={'slug': 'test-post-slug'})
        assert path, PostUpdateView.as_view().__name__

    def test_post_delete(self):
        """ Verify that the `post_delete` url invokes intended view """
        path = reverse('blog:post_delete', kwargs={'slug': 'test-post-slug'})
        assert path, PostDeleteView.as_view().__name__

    def test_search(self):
        """ Verify that the `search` url invokes intended view """
        path = reverse('blog:search')
        assert path, SearchView.as_view().__name__

    def test_search_results(self):
        """ Verify that the `search results` url invokes intended view """
        path = reverse('blog:search_results')
        assert path, SearchResultsView.as_view().__name__

    def test_index(self):
        """ Verify that the `index` url invokes intended view """
        path = reverse('blog:index')
        assert path, IndexListView.as_view().__name__

    def test_contents(self):
        """ Verify that the `contents` url invokes intended view """
        path = reverse('blog:contents')
        assert path, ContentsListView.as_view().__name__
