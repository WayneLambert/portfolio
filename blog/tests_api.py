from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse
from django.utils.timezone import now
from blog.models import Post


class TestPostModelViewSet(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_can_create_post(self):
        """ Ensure we can create a new post """
        data = {
            'title': 'Test Blog Title',
            'slug': reverse('test-blog-title'),
            'content': reverse('test-blog-title'),
            'reference_url': reverse('http:///www.example.com'),
            'publish_date': now(),
            'updated_date': now(),
            'status': 0,
            'author': 2,
            'categories': 2,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 3)

    def test_post_detail_view(self):
        post_id = Post.objects.first().id
        detail_url = self.url + '/' + str(post_id)
        response = self.client.get(detail_url, format='json')
        self.assertEqual((response.status_code, 200))
