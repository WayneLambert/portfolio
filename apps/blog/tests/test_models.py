import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

import pytest

from mixer.backend.django import mixer
from tinymce.models import HTMLField

from apps.blog.models import Category, Post


pytestmark = pytest.mark.django_db(reset_sequences=True)


user_model = get_user_model()

class TestCategory:
    def test_name_is_charfield(self):
        category = mixer.blend(Category, pk=1)
        field = category._meta.get_field("name")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_slug_is_slugfield(self):
        category = mixer.blend(Category, pk=1)
        field = category._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_created_date_is_datefield(self):
        category = mixer.blend(Category, pk=1)
        field = category._meta.get_field("created_date")
        assert isinstance(field, models.DateField), 'Should be a date field'

    def test_category_str(self):
        category = mixer.blend(Category, pk=1, name='Python')
        assert str(category) == 'Python', 'Should be the same as the category name'

    def test_get_absolute_url(self):
        category = mixer.blend(Category, pk=1, title='Example Category', slug='example-category')
        assert category.get_absolute_url() == \
            reverse('blog:category_posts', kwargs={'slug': category.slug})


class TestPost:
    def test_title_is_charfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("title")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_slug_is_slugfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_slugification(self):
        post = mixer.blend(Post, author__pk=2)
        post.slug = slugify(post.title)
        title_fragments = post.title.split()
        for fragment in title_fragments:
            assert fragment.casefold() in post.slug
        if len(title_fragments) > 1:
            assert '-' in post.slug, 'Should contain a hyphen'

    def test_unique_slug_created(self):
        post1 = mixer.blend(Post, author__pk=2, slug='example-slug')
        post1.save()
        post2 = mixer.blend(Post, author__pk=2, slug='example-slug')
        post2.save()
        assert post2.slug != post1.slug, 'Should be different slugs'
        assert post2.slug == f"{post1.slug}1", 'Should append a new count to the slug'

    def test_content_is_htmlfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("content")
        assert isinstance(field, HTMLField), \
            'Should be an `HTML Field` from third party app, Django Tiny MCE'

    def test_reference_url_is_urlfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("reference_url")
        assert isinstance(field, models.URLField), 'Should be a URL field'

    def test_publish_date_is_datetimefield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("publish_date")
        assert isinstance(field, models.DateTimeField), 'Should be a datetime field'

    def test_publish_date_generates(self):
        post = mixer.blend(Post, author__pk=2)
        assert post.publish_date.day == datetime.date.today().day, \
            'Should generate the day of the week for today'

    def test_updated_date_is_datetimefield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("updated_date")
        assert isinstance(field, models.DateTimeField), 'Should be a datetime field'

    def test_updated_date_generates(self):
        post = mixer.blend(Post, author__pk=2)
        assert post.updated_date.day == datetime.date.today().day, \
            'Should generate the day of the week for today'

    def test_image_is_imagefield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("image")
        assert isinstance(field, models.ImageField), 'Should be an image field'

    def test_status_is_integerfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("status")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_status_defaults_as_draft(self):
        post = mixer.blend(Post, author__pk=2)
        assert post.status == 0, 'Should default to `0`'

    def test_author_is_foreignkeyfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("author")
        assert isinstance(field, models.ForeignKey), 'Should be a foreign key field'

    def test_categories_is_manytomanyfield(self):
        post = mixer.blend(Post, author__pk=2)
        field = post._meta.get_field("categories")
        assert isinstance(field, models.ManyToManyField), 'Should be a many-to-many field'

    def test_word_count(self):
        post = mixer.blend(Post, author__pk=2, content='Beautiful is better than ugly.')
        assert post.word_count == 5, \
            'Calculated word count should be the number of words in the content string'

    def test_reading_time(self):
        test_text = 'lorem ipsum '
        post = mixer.blend(Post, author__pk=2, content=test_text * 50)
        assert post.reading_time == 2, \
            'The duplicated lorem ipsum text of 100 words should be a 2 minute read'

    def test_get_excerpt(self):
        post = mixer.blend(Post, author__pk=2, content='Test content ...')
        result = post.get_excerpt(16)
        assert result == 'Test content ...', 'Should return first 16 characters'

    def test_post_str(self):
        post = mixer.blend(Post, author__pk=2, title='Example Post')
        assert str(post) == 'Example Post', 'Should be the same as the post name'

    def test_publish_year(self):
        post = mixer.blend(Post, author__pk=2)
        assert post.publish_year == post.publish_date.year, \
            "Year should be the same as the published date's year property"

    def test_num_draft_posts(self):
        draft_posts = mixer.cycle(10).blend(Post, author__pk=2, status=0)
        published_posts = mixer.cycle(5).blend(Post, author__pk=2, status=1)
        total_posts = draft_posts + published_posts
        assert len(total_posts) == Post.objects.count(), 'Should have 15 posts in the DB'
        assert Post.num_draft_posts() == 10, 'Should have 10 `draft` posts in the DB'

    def test_published_posts_manager(self):
        draft_posts = mixer.cycle(10).blend(Post, author__pk=2, status=0)
        published_posts = mixer.cycle(5).blend(Post, author__pk=2, status=1)
        total_posts = draft_posts + published_posts
        assert len(total_posts) == Post.objects.count(), 'Should have 15 posts in the DB'
        assert Post.published.count() == 5, 'Should have 5 `published` posts in the DB'

    def test_get_absolute_url(self):
        post = mixer.blend(Post, author__pk=2, title='Example Post', slug='example-post')
        assert post.get_absolute_url() == reverse('blog:post_detail', kwargs={'slug': post.slug})

    def test_multiple_post_slugs_appends_instance_id(self):
        posts = mixer.cycle(10).blend(Post, author__pk=2, title='Example Post', slug='example-post')
        assert posts[9].pk == 10, '10th instance should have a PK of 10'
        assert Post.objects.count() == 10, 'Should have 10 objects in the database'
        assert posts[9].slug == 'example-post9', '10th instance of DB save appends next id'
