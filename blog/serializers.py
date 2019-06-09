from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False, allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'publish_date',
            'updated_date',
            'upvotes',
            'downvotes',
            'image',
        )
        ordering = ['-publish_date']

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['publish_date'] = instance.publish_date.strftime(format='%a %d-%b-%Y %H:%M')
        representation['updated_date'] = instance.updated_date.strftime(format='%a %d-%b-%Y %H:%M')
        return representation
