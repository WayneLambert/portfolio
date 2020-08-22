from django.urls import include, path

from apps.api.views import CategoryListAPIView, PostDetailAPIView, PostListAPIView


app_name = 'api'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('blog/posts/', PostListAPIView.as_view(), name='posts'),
    path('blog/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('blog/categories/', CategoryListAPIView.as_view(), name='blog_categories'),
]
