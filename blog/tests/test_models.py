import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestCategory:
    def test_category_model(self):
        category = mixer.blend('blog.Category')
        assert category.pk == 1, 'Should create a Category instance'


class TestPost:
    def test_post_model(self):
        post = mixer.blend('blog.Post')
        assert post.pk == 1, 'Should create a Post instance'

    def test_get_excerpt(self):
        post = mixer.blend('blog.Post', content='Test content ...')
        result = post.get_excerpt(16)
        assert result == 'Test content ...', 'Should return first 16 characters'
