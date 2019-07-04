from django.urls import path
from blog.views import (CategoryPostListView, PostCreateView, PostDeleteView,
                        PostDetailView, PostListView, PostUpdateView,
                        UserPostListView, SearchResultsView, get_contents_page)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/<slug:slug>/',
         CategoryPostListView.as_view(), name='category-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('contents/', get_contents_page, name='contents'),
]
