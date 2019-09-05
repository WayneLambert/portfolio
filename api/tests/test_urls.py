from django.urls import resolve, reverse


class TestUrls:
    def test_blog_api(self):
        path = reverse('blog-api')
        assert resolve(path).view_name == 'blog-api'

    def test_blog_posts_api(self):
        path = reverse('blog-posts-api', kwargs={'pk': 1})
        assert resolve(path).view_name == 'blog-posts-api'

    def test_blog_categories_api(self):
        path = reverse('blog-categories-api')
        assert resolve(path).view_name == 'blog-categories-api'
