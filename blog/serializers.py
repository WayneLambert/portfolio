from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Category, Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False, allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
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

    def to_representation(self, instance):
        representation = super(CategorySerializer, self).to_representation(instance)
        representation['created_date'] = instance.created_date.strftime(format='%a %d-%b-%Y')
        return representation


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Post

        def get_status(self, obj):
            return obj.get_status_display()

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
            'author_username',
            'categories',
        )

        ordering = ['-publish_date']
