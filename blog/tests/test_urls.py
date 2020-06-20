from django.urls import reverse

from blog.views import (CategoryPostListView, ContentsListView, HomeView, IndexListView,
                        PostCreateView, PostDeleteView, PostDetailView, PostUpdateView,
                        SearchResultsView, UserPostListView)


class TestUrls:

    def test_blog_home(self):
        path = reverse('blog:home')
        assert path, HomeView.as_view().__name__

    def test_user_posts(self):
        path = reverse('blog:user_posts', kwargs={'username': 'test-username'})
        assert path, UserPostListView.as_view().__name__

    def test_category_posts(self):
        path = reverse('blog:category_posts', kwargs={'slug': 'test-category-slug'})
        assert path, CategoryPostListView.as_view().__name__

    def test_post_create(self):
        path = reverse('blog:post_create')
        assert path, PostCreateView.as_view().__name__

    def test_post_detail(self):
        path = reverse('blog:post_detail', kwargs={'slug': 'test-post-slug'})
        assert path, PostDetailView.as_view().__name__

    def test_post_update(self):
        path = reverse('blog:post_update', kwargs={'slug': 'test-post-slug'})
        assert path, PostUpdateView.as_view().__name__

    def test_post_delete(self):
        path = reverse('blog:post_delete', kwargs={'slug': 'test-post-slug'})
        assert path, PostDeleteView.as_view().__name__

    def test_search_results(self):
        path = reverse('blog:search_results')
        assert path, SearchResultsView.as_view().__name__

    def test_contents(self):
        path = reverse('blog:contents')
        assert path, ContentsListView.as_view().__name__

    def test_inde(self):
        path = reverse('blog:index')
        assert path, IndexListView.as_view().__name__
