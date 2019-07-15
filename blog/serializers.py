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
        representation['created_date'] = instance.created_date.strftime(format='%a %d-%b-%Y %H:%M')
        return representation


class PostSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    # author_username = serializers.CharField(source='author.username')
    # status = serializers.ChoiceField(choices=Post.Status)

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
            'author_username',
            'categories',
        )
        read_only_fields = (
            'id',
            'categories',
        )
        ordering = ['-publish_date']

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['publish_date'] = instance.publish_date.strftime(format='%a %d-%b-%Y %H:%M')
        representation['updated_date'] = instance.updated_date.strftime(format='%a %d-%b-%Y %H:%M')
        return representation
