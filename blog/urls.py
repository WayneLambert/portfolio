from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    about
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),
]

"""
The urls configuration below is a for a DRF setup with a fully segregrated
front end using React.
"""

# from rest_framework.routers import DefaultRouter
# from blog.views import PostViewSet

# router = DefaultRouter()
# router.register('', PostViewSet, basename='posts')
# urlpatterns = router.urls
