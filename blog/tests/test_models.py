import datetime
import pytest
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from mixer.backend.django import mixer

from blog.models import Category, Post

pytestmark = pytest.mark.django_db

user_model = get_user_model()

class TestCategory:
    def test_single_category_save(self):
        category = mixer.blend(Category)
        assert category.pk == 1, 'Should create a `Category` instance'

    def test_multi_category_saves(self):
        categories = mixer.cycle(10).blend(Category)
        assert categories[9].pk == 10, '10th instance should have a PK of 10'
        assert Category.objects.count() == 10, 'Should have 10 objects in the database'

    def test_can_delete_category(self):
        categories = mixer.cycle(10).blend(Category)
        categories[4].delete()
        assert Category.objects.count() == 9, \
            'Should have 9 objects remaining in the database'

    def test_name_is_charfield(self):
        category = mixer.blend(Category)
        field = category._meta.get_field("name")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_slug_is_slugfield(self):
        category = mixer.blend(Category)
        field = category._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_created_date_is_datefield(self):
        category = mixer.blend(Category)
        field = category._meta.get_field("created_date")
        assert isinstance(field, models.DateField), 'Should be a date field'

class TestPost:
    def test_single_post_save(self):
        post = mixer.blend(Post)
        assert post.pk == 1, 'Should create a `Post` instance'

    def test_multi_post_saves(self):
        posts = mixer.cycle(10).blend(Post)
        assert posts[9].pk == 10, '10th instance should have a PK of 10'
        assert Post.objects.count() == 10, 'Should have 10 objects in the database'

    def test_can_delete_post(self):
        posts = mixer.cycle(10).blend(Post)
        posts[4].delete()
        assert Post.objects.count() == 9, \
            'Should have 9 objects remaining in the database'

    def test_title_is_charfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("title")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_slug_is_slugfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_slugification(self):
        post = mixer.blend(Post)
        post.slug = slugify(post.title)
        post_fragments = post.title.split()
        for post_fragment in post_fragments:
            assert post_fragment.casefold() in post.slug
        if len(post_fragments) > 1:
            assert '-' in post.slug, 'Should contain a hyphen'

    def test_content_is_richtextuploadingfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("content")
        assert isinstance(field, RichTextUploadingField), \
            'Should be a `Rich Text Uploading Field` from third party app, CK Editor'

    def test_reference_url_is_urlfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("reference_url")
        assert isinstance(field, models.URLField), 'Should be a URL field'

    def test_publish_date_is_datetimefield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("publish_date")
        assert isinstance(field, models.DateTimeField), 'Should be a datetime field'

    def test_publish_date_generates(self):
        post = mixer.blend(Post)
        assert post.publish_date.day == datetime.date.today().day

    def test_updated_date_is_datetimefield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("updated_date")
        assert isinstance(field, models.DateTimeField), 'Should be a datetime field'

    def test_updated_date_generates(self):
        post = mixer.blend(Post)
        assert post.updated_date.day == datetime.date.today().day

    def test_image_is_imagefield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("image")
        assert isinstance(field, models.ImageField), 'Should be an image field'

    def test_status_is_integerfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("status")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_status_defaults_as_draft(self):
        post = mixer.blend(Post)
        assert post.status == 0, 'Should default to `0`'

    def test_author_is_foreignkeyfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("author")
        assert isinstance(field, models.ForeignKey), 'Should be a foreign key field'

    def test_categories_is_manytomanyfield(self):
        post = mixer.blend(Post)
        field = post._meta.get_field("categories")
        assert isinstance(field, models.ManyToManyField), 'Should be a many-to-many field'

    def test_get_excerpt(self):
        post = mixer.blend(Post, content='Test content ...')
        result = post.get_excerpt(16)
        assert result == 'Test content ...', 'Should return first 16 characters'
