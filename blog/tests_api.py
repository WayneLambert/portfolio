from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import include, path, reverse
from django.utils.timezone import now
from blog.models import Post


class TestPostModelViewSet(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_create_post(self):
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

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(Post.objects.get().title, 'Test Blog Title')
        self.assertEqual(Post.objects.get().slug, 'test-blog-title')
        self.assertEqual(Post.objects.get().reference_url, 'test-blog-title')
