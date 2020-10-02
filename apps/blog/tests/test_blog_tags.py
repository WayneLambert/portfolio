import pytest

from mixer.backend.django import mixer

from apps.blog.models import Category
from apps.blog.templatetags.blog_tags import category_sidebar


pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestCategorySidebar:
    def test_category_sidebar(self):
        """ Asserts blog_categories context contains all categories """
        categories = mixer.cycle(10).blend(Category)
        assert categories[9].pk == 10, '10th instance should have a PK of 10'
        assert Category.objects.count() == 10, 'Should have 10 objects in the database'
        blog_categories = category_sidebar()
        qs = blog_categories['blog_categories']
        assert qs.count() == 10, 'Queryset should contain 10 categories'
