from django.urls import path, re_path

from blog.views import (CategoryPostListView, PostCreateView, PostDeleteView,
                        PostDetailView, PostListView, PostUpdateView,
                        UserPostListView, about)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/<slug:slug>/',
         CategoryPostListView.as_view(), name='category-posts'),
    re_path(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
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
