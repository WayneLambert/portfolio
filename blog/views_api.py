from rest_framework import generics
from blog.serializers import CategorySerializer, PostSerializer
from blog.models import Category, Post


class CategoryListAPIView(generics.ListCreateAPIView):
    """ API endpoint that enables category list to be viewed. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fields = ('name')


class PostListAPIView(generics.ListCreateAPIView):
    """ API endpoint that enables post list to be viewed. """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_fields = ('title')


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint that enables post instances to be viewed or edited. """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
