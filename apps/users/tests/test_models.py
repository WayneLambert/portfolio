# pylint: disable=redefined-outer-name
import pytest

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixer.backend.django import mixer

from apps.users.models import Profile


@pytest.mark.django_db
class TestProfile:
    def test_single_profile_save(self, fixed_user):
        assert fixed_user.pk == 2, 'Should create a `User` instance'
        assert fixed_user.user.pk == 2, \
            'Through Django signals, should create both a `Profile` instance too. \
                NOTE: pk=1 is AnonymousUser'

    def test_multi_profile_saves(self):
        mixer.cycle(10).blend(get_user_model())
        assert get_user_model().objects.count() == 11, 'Should have 11 objects in the database'
        assert Profile.objects.count() == 11, 'Should have 11 objects in the database'

    def test_can_delete_profile(self):
        """
        If you add a `User`, you also add a `Profile` through Django signals.
        If you delete a `User`, you also delete their `Profile` (on_delete=models.CASCADE)
        If you delete the `Profile`, only the profile is deleted.
        """
        users = mixer.cycle(10).blend(get_user_model())
        users[4].delete()
        assert get_user_model().objects.count() == 10, \
            'Should have 9 objects remaining in the database'
        assert Profile.objects.count() == 10, 'Should have 9 objects remaining in the database'
        Profile.objects.get(pk=4).delete()
        assert Profile.objects.count() == 9, 'Should have 9 objects remaining in the database'
        assert get_user_model().objects.count() == 10, 'Should still equal 10'

    def test_user_is_onetoonefield(self):
        user = mixer.blend(get_user_model())
        field = user.user._meta.get_field("user")
        assert isinstance(field, models.OneToOneField), 'Should be a one-to-one field'

    def test_slug_is_slugfield(self):
        user = mixer.blend(get_user_model())
        field = user.user._meta.get_field("slug")
        assert isinstance(field, models.SlugField), 'Should be a slug field'

    def test_slugification(self):
        user = mixer.blend(get_user_model())
        user.user.slug = slugify(user.user.full_name)
        profile_slug_fragments = user.user.slug.split('-')
        for fragment in profile_slug_fragments:
            assert fragment.casefold() in user.user.slug
        if len(profile_slug_fragments) > 1:
            assert '-' in user.user.slug, 'Should contain a hyphen'

    def test_author_view_is_integerfield(self):
        user = mixer.blend(get_user_model())
        field = user.user._meta.get_field("author_view")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_profile_picture_is_imagefield(self):
        user = mixer.blend(get_user_model())
        field = user.user._meta.get_field("profile_picture")
        assert isinstance(field, models.ImageField), 'Should be an image date field'

    def test_full_name(self, fixed_user):
        get_user_model().objects.create(
            first_name=fixed_user.first_name,
            last_name=fixed_user.last_name,
            email=fixed_user.email
        )
        profile = Profile.objects.get(slug='wayne-lambert')
        assert profile.full_name == 'Wayne Lambert', 'Should be first and last name concatenated'

    def test_profile_str(self, fixed_user):
        assert fixed_user.pk == 2, 'User instance should be set up'
        assert fixed_user.user.pk == 2, 'Profile instance with signal should be set up'
        assert str(Profile.objects.get(slug='wayne-lambert')) == 'Wayne Lambert (wayne-lambert)', \
            '__str__ method should be formatted'

    def test_join_year(self):
        user = mixer.blend(get_user_model())
        assert user.user.join_year == user.date_joined.year, \
            "Year should be the same as the `date_joined` field year property"

    def test_get_absolute_url(self):
        user = mixer.blend(get_user_model())
        assert user.user.get_absolute_url() == reverse(
            'blog:users:profile', kwargs={'username': user.user.slug}), 'Should resolve the URL'
