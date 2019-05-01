from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.RelatedField(source='author', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author_name', 'publish_date', 'updated_date')
        ordering = ['-publish_date']

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['author_name'] = instance.author_name
        representation['publish_date'] = instance.publish_date.strftime(format='%d-%m-%Y %H:%M')
        representation['updated_date'] = instance.updated_date.strftime(format='%d-%m-%Y %H:%M')
        return representation
