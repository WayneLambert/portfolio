from django.urls import include, path
from blog.views_api import (
    PostListAPIView,
    PostDetailAPIView,
    CategoryListAPIView,
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('blog/posts/', PostListAPIView.as_view()),
    path('blog/posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('blog/categories/', CategoryListAPIView.as_view()),
]
