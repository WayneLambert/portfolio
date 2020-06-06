from django.urls import path

from .feeds import LatestPostsFeed
from .views import (CategoryPostListView, ContentsListView, HomeView,
                    PostCreateView, PostDeleteView, PostDetailView,
                    PostUpdateView, SearchResultsView, UserPostListView)

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contents/', ContentsListView.as_view(), name='contents'),
    path('feed/latest/rss', LatestPostsFeed(), name='post_feed'),
]
