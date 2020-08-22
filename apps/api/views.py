from rest_framework import generics

from apps.api.serializers import CategorySerializer, PostSerializer
from apps.blog.models import Category, Post


class CategoryListAPIView(generics.ListAPIView):
    """ API endpoint that enables category list to be viewed. """
    queryset = Category.objects.all().prefetch_related('posts')
    serializer_class = CategorySerializer
    lookup_fields = ('name')


class PostListAPIView(generics.ListAPIView):
    """ API endpoint that enables post list to be viewed. """
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')
    serializer_class = PostSerializer
    lookup_fields = ('title')


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint that enables post instances to be viewed or edited. """
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')
    serializer_class = PostSerializer
