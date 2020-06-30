from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Category, Post
from users.models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )

class ProfileSerializer(serializers.ModelSerializer):

    full_name = serializers.Field()

    class Meta:
        model = Profile
        fields = (
            'user',
            'slug',
            'author_view',
            'profile_picture',
            'full_name',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'created_date',
        )
        ordering = ['name']


class PostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    word_count = serializers.CharField()
    reading_time = serializers.CharField()
    author_username = serializers.CharField(source='author.username')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_full_name = serializers.CharField(source='author.user.full_name')
    author_view = serializers.IntegerField(source='author.user.author_view')
    profile_picture = serializers.ImageField(source='author.user.profile_picture')
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'reference_url',
            'publish_date',
            'updated_date',
            'image',
            'status',
            'word_count',
            'reading_time',
            'author_username',
            'author_first_name',
            'author_last_name',
            'author_full_name',
            'author_view',
            'profile_picture',
            'categories',
        )

        def get_status(self, obj):
            return obj.get_status_display()

        ordering = ['-updated_date', '-publish_date']
