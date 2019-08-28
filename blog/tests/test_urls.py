from django.urls import resolve, reverse

class TestUrls:

    def test_blog_django_home(self):
        path = reverse('blog-django')
        assert resolve(path).view_name == 'blog-django'

    def test_user_posts(self):
        path = reverse('user-posts', kwargs={'username': 'test-username'})
        assert resolve(path).view_name == 'user-posts'

    def test_category_posts(self):
        path = reverse('category-posts', kwargs={'slug': 'test-category-slug'})
        assert resolve(path).view_name == 'category-posts'

    def test_post_create(self):
        path = reverse('post-create')
        assert resolve(path).view_name == 'post-create'

    def test_post_detail(self):
        path = reverse('post-detail', kwargs={'slug': 'test-post-slug'})
        assert resolve(path).view_name == 'post-detail'

    def test_post_update(self):
        path = reverse('post-update', kwargs={'slug': 'test-post-slug'})
        assert resolve(path).view_name == 'post-update'

    def test_post_delete(self):
        path = reverse('post-delete', kwargs={'slug': 'test-post-slug'})
        assert resolve(path).view_name == 'post-delete'

    def test_search_results(self):
        path = reverse('search-results')
        assert resolve(path).view_name == 'search-results'

    def test_contents(self):
        path = reverse('contents')
        assert resolve(path).view_name == 'contents'
