from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
