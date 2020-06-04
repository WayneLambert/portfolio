from django.urls import include, path
from blog.views_api import (
    PostListAPIView,
    PostDetailAPIView,
    CategoryListAPIView,
)

app_name = 'api'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('blog/posts/', PostListAPIView.as_view(), name='blog-api'),
    path('blog/posts/<int:pk>/', PostDetailAPIView.as_view(), name='blog-posts-api'),
    path('blog/categories/', CategoryListAPIView.as_view(), name='blog-categories-api'),
]
