from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import pytest

from mixer.backend.django import mixer

from apps.users.models import Profile


@pytest.mark.django_db
class TestProfile:
    def test_single_profile_save(self, fixed_user):
        assert fixed_user.pk == 2, 'Should create a `User` instance'
        assert fixed_user.user.pk == 2, \
            'Through Django signals, should create both a `Profile` instance too. \
                NOTE: pk=1 is AnonymousUser'

    def test_multi_profile_saves(self, django_user_model):
        mixer.cycle(10).blend(django_user_model)
        assert django_user_model.objects.count() == 11, 'Should have 11 objects in the database'
        assert Profile.objects.count() == 11, 'Should have 11 objects in the database'

    def test_can_delete_profile(self, django_user_model):
        """
        If you add a `User`, you also add a `Profile` through Django signals.
        If you delete a `User`, you also delete their `Profile` (on_delete=models.CASCADE)
        If you delete the `Profile`, only the profile is deleted.
        """
        users = mixer.cycle(10).blend(django_user_model)
        users[4].delete()
        assert django_user_model.objects.count() == 10, \
            'Should have 9 objects remaining in the database'
        assert Profile.objects.count() == 10, 'Should have 9 objects remaining in the database'
        Profile.objects.get(pk=4).delete()
        assert Profile.objects.count() == 9, 'Should have 9 objects remaining in the database'
        assert django_user_model.objects.count() == 10, 'Should still equal 10'

    def test_user_is_onetoonefield(self, random_user):
        field = random_user.user._meta.get_field("user")
        assert isinstance(field, models.OneToOneField), 'Should be a one-to-one field'

    def test_slug_is_slugfield(self, random_user):
        field = random_user.user._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_slugification(self, random_user):
        random_user.user.slug = slugify(random_user.username)
        profile_slug_fragments = random_user.user.slug.split('-')
        for fragment in profile_slug_fragments:
            assert fragment.casefold() in random_user.user.slug
        if len(profile_slug_fragments) > 1:
            assert '-' in random_user.user.slug, 'Should contain a hyphen'

    def test_author_view_is_integerfield(self, random_user):
        field = random_user.user._meta.get_field("author_view")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_profile_picture_is_imagefield(self, random_user):
        field = random_user.user._meta.get_field("profile_picture")
        assert isinstance(field, models.ImageField), 'Should be an image date field'

    def test_created_date_is_datetimefield(self, random_user):
        field = random_user.user._meta.get_field("created_date")
        assert isinstance(field, models.DateTimeField), 'Should be an image date field'

    def test_updated_date_is_imagefield(self, random_user):
        field = random_user.user._meta.get_field("updated_date")
        assert isinstance(field, models.DateTimeField), 'Should be an image date field'

    def test_full_name(self, fixed_user):
        assert fixed_user.user.full_name == 'Wayne Lambert', 'Concatenation of first and last name'

    def test_profile_str(self, fixed_user):
        assert fixed_user.pk == 2, 'User instance should be set up'
        assert fixed_user.user.pk == 2, 'Profile instance with signal should be set up'
        assert str(Profile.objects.get(slug='wayne-lambert')) == 'Wayne Lambert (wayne-lambert)', \
            '__str__ method should be formatted'

    def test_initials(self, fixed_user):
        assert fixed_user.user.initials == 'WL', 'Should be first letter of first and last name'

    def test_join_year(self, random_user):
        assert random_user.user.join_year == random_user.date_joined.year, \
            "Year should be the same as the `date_joined` field year property"

    def test_display_name_is_username(self, random_user):
        random_user.user.author_view = 0
        assert random_user.user.display_name == random_user.username, 'Should be the username'

    def test_display_name_is_full_name(self, random_user):
        random_user.user.author_view = 1
        assert random_user.user.display_name == random_user.user.full_name, \
            "Should be the user's full name"

    def test_get_absolute_url(self, random_user):
        assert random_user.user.get_absolute_url() == reverse(
            'blog:users:profile', kwargs={'username': random_user.user.slug}), 'Should resolve URL'
