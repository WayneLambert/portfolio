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
    categories = serializers.StringRelatedField(many=True)
    author_username = serializers.CharField(source='author.username')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
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
            'author_first_name',
            'author_last_name',
            'categories',
        )
        read_only_fields = (
            'id',
            'author_first_name',
            'author_last_name',
        )
        ordering = ['-publish_date']

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['publish_date'] = instance.publish_date.strftime(format='%a %d-%b-%Y')
        representation['updated_date'] = instance.updated_date.strftime(format='%a %d-%b-%Y')
        return representation
