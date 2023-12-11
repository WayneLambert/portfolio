from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import pytest

pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestProfile:
    def test_user_is_onetoonefield(self, random_user):
        field = random_user.profile._meta.get_field("user")
        assert isinstance(field, models.OneToOneField), "Should be a one-to-one field"

    def test_slug_is_slugfield(self, random_user):
        field = random_user.profile._meta.get_field("slug")
        assert isinstance(field, models.SlugField), "Should be a slug field"

    def test_slugification(self, random_user):
        random_user.profile.slug = slugify(random_user.username)
        profile_slug_fragments = random_user.profile.slug.split("-")
        for fragment in profile_slug_fragments:
            assert fragment.casefold() in random_user.profile.slug
        if len(profile_slug_fragments) > 1:
            assert "-" in random_user.profile.slug, "Should contain a hyphen"

    def test_author_view_is_integerfield(self, random_user):
        field = random_user.profile._meta.get_field("author_view")
        assert isinstance(field, models.IntegerField), "Should be an integer field"

    def test_profile_picture_is_imagefield(self, random_user):
        field = random_user.profile._meta.get_field("profile_picture")
        assert isinstance(field, models.ImageField), "Should be an image date field"

    def test_created_date_is_datetimefield(self, random_user):
        field = random_user.profile._meta.get_field("created_date")
        assert isinstance(field, models.DateTimeField), "Should be an image date field"

    def test_updated_date_is_imagefield(self, random_user):
        field = random_user.profile._meta.get_field("updated_date")
        assert isinstance(field, models.DateTimeField), "Should be an image date field"

    def test_profile_str(self, fixed_user):
        assert fixed_user.pk == 2, "User instance should be set up"
        assert fixed_user.profile.pk == 2, "Profile instance with signal should be set up"
        assert (
            fixed_user.profile.__str__() == "Wayne Lambert (wayne-lambert)"
        ), "__str__ method should be formatted"

    def test_initials(self, fixed_user):
        assert fixed_user.profile.initials == "WL", "Should be first letter of first and last name"

    def test_join_year(self, random_user):
        assert (
            random_user.profile.join_year == random_user.date_joined.year
        ), "Year should be the same as the `date_joined` field year property"

    def test_display_name_is_username(self, random_user):
        random_user.profile.author_view = 0
        assert (
            random_user.profile.display_name == random_user.get_username()
        ), "Should be the user's username"

    def test_display_name_is_full_name(self, random_user):
        random_user.profile.author_view = 1
        assert (
            random_user.profile.display_name == random_user.get_full_name()
        ), "Should be the user's full name"

    def test_get_absolute_url(self, random_user):
        assert random_user.profile.get_absolute_url() == reverse(
            "blog:users:profile", kwargs={"username": random_user.profile.slug}
        ), "Should resolve URL"
