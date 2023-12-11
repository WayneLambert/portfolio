from django.urls import reverse

from apps.api.views import CategoryListAPIView, PostDetailAPIView, PostListAPIView


class TestURLs:
    def test_category_list_api_url(self):
        """Verify that the `/api/blog/categories/` url invokes intended view"""
        path = reverse("api:blog_categories")
        assert path, CategoryListAPIView.as_view().__name__

    def test_post_list_api_url(self):
        """Verify that the `/api/blog/posts/` url invokes intended view"""
        path = reverse("api:posts")
        assert path, PostListAPIView.as_view().__name__

    def test_post_detail_api_url(self):
        """Verify that the `/api/blog/posts/3/` url invokes intended view"""
        path = reverse("api:post_detail", kwargs={"pk": 3})
        assert path, PostDetailAPIView.as_view().__name__
