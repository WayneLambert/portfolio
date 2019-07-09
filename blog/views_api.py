from rest_framework import generics
from blog.serializers import PostSerializer
from blog.models import Post


class PostListAPI_View(generics.ListCreateAPIView):
    """ API endpoint that enables post list to be viewed. """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI_View(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint that enables post instances to be viewed or edited. """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
