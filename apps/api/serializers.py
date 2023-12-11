from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.blog.models import Category, Post
from apps.users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
        )


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.Field()

    class Meta:
        model = Profile
        fields = (
            "user",
            "slug",
            "author_view",
            "profile_picture",
            "full_name",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "created_date",
        )
        ordering = ["name"]


class PostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    word_count = serializers.IntegerField()
    reading_time = serializers.IntegerField()
    post_absolute_url = serializers.URLField(source="get_absolute_url")

    author_username = serializers.CharField(source="author.get_username")
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    author_full_name = serializers.CharField(source="author.get_full_name")
    author_initials = serializers.CharField(source="author.profile.initials")
    author_display_name = serializers.CharField(source="author.profile.display_name")
    author_join_year = serializers.IntegerField(source="author.profile.join_year")
    author_view = serializers.IntegerField(source="author.profile.author_view")
    author_created_date = serializers.DateTimeField(source="author.profile.created_date")
    author_updated_date = serializers.DateTimeField(source="author.profile.updated_date")
    author_absolute_url = serializers.URLField(source="author.profile.get_absolute_url")
    author_profile_picture = serializers.ImageField(source="author.profile.profile_picture")

    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            # Post fields
            "id",
            "title",
            "slug",
            "content",
            "reference_url",
            "publish_date",
            "updated_date",
            "image",
            "status",
            "word_count",
            "reading_time",
            "post_absolute_url",
            # Author fields
            "author_username",
            "author_first_name",
            "author_last_name",
            "author_full_name",
            "author_initials",
            "author_display_name",
            "author_join_year",
            "author_view",
            "author_created_date",
            "author_updated_date",
            "author_absolute_url",
            "author_profile_picture",
            # Category fields
            "categories",
        )

    def get_status(self, obj):
        return obj.get_status_display()  # pragma: no cover

    ordering = (
        "-updated_date",
        "-publish_date",
    )
