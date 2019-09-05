"""
These unit tests are not actually used as I favour the PyTest framework for testing.
They exist in the project's code for demonstration purposes of using Django's
standard unitest framework.
"""


from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post


class BlogTests(TestCase):
    try:
        from unittest.mock import MagicMock
    except:
        from mock import MagicMock

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username='michael_jackson', password='billiejean'
        )
        testuser.save()

        test_post = Post.objects.create(
            title='Blog title',
            slug='blog-title',
            content='Body content...',
            url='www.example.com',
            author=testuser.username,
            publish_date=datetime.now(),
            status=1,
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_slug = f'{post.slug}'
        expected_content = f'{post.content}'
        expected_url = f'{post.reference_url}'
        expected_author = f'{post.author}'
        expected_publish_date = f'{post.publish_date}'
        expected_status = f'{post.status}'
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_slug, 'blog-title')
        self.assertEqual(expected_content, 'Body content...')
        self.assertEqual(expected_url, 'www.example.com')
        self.assertEqual(expected_author, 'michael_jackson')
        self.assertGreaterEqual(expected_publish_date, datetime.now())
        self.assertEqual(expected_status, 1)
