from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.api.serializers import CategorySerializer, PostSerializer
from apps.blog.models import Category, Post


class CategoryListAPIView(ListAPIView):
    """
    API endpoint that enables a list of categories to be browsed.

    The configured endpoint purposefully does not permit a POST method
    as I do not want others creating new categories in the database.
    """
    name = "Category List API"
    queryset = Category.objects.all().prefetch_related('posts')
    serializer_class = CategorySerializer
    lookup_fields = ('name')


class PostListAPIView(ListAPIView):
    """
    API endpoint that enables a list of posts to be browsed including
    related models data and auxhiliary properties.

    The configured endpoint purposefully does not permit a POST method
    as I do not want others creating new posts in the database.
    """
    name = "Post List API"
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')
    serializer_class = PostSerializer
    lookup_fields = ('title')


class PostDetailAPIView(RetrieveAPIView):
    """
    API endpoint that enables a single post instance to be browsed.

    The configured endpoint uses a RetrieveAPIView to limit to read-only
    access. I do not others creating new posts in the database.
    """
    name = "Post Detail API"
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')
    serializer_class = PostSerializer
