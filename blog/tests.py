from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from datetime import datetime


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username='michael_jackson', password='billiejean'
        )
        testuser.save()

        test_post = Post.objects.create(
            title='Blog title',
            slug='blog-title',
            body='Body content...',
            author=testuser,
            publish_date=datetime.now(),
            status=1,
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_slug = f'{post.slug}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        expected_publish_date = f'{post.publish_date}'
        expected_status = f'{post.status}'
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_slug, 'blog-title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'michael_jackson')
        self.assertGreaterEqual(expected_publish_date, datetime.now())
        self.assertEqual(expected_status, 1)
