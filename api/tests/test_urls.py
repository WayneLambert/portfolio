from django.urls import resolve, reverse


class TestUrls:
    def test_blog_api(self):
        path = reverse('posts')
        assert resolve(path).view_name == 'posts'

    def test_blog_posts_api(self):
        path = reverse('post_detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'post_detail'

    def test_blog_categories_api(self):
        path = reverse('blog_categories')
        assert resolve(path).view_name == 'blog_categories'
