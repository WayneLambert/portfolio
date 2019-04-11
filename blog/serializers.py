from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'author', 'publish_date', 'updated_date')
        model = Post
