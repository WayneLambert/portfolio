from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username='michael_jackson', password='billiejean'
        )
        testuser.save()

        test_post = Post.objects.create(
            title='Blog title', body='Body content...', author=testuser
            )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'michael_jackson')
