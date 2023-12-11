from django.urls import include, path

from apps.blog.feeds import AtomLatestPostsFeed, LatestPostsFeed
from apps.blog.views import (
    AuthorPostListView,
    CategoryPostListView,
    ContentsListView,
    HomeView,
    IndexListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView,
    SearchResultsView,
    SearchView,
)


app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("user/<str:username>/posts", AuthorPostListView.as_view(), name="author_posts"),
    path("category/<slug:slug>/posts", CategoryPostListView.as_view(), name="category_posts"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("search/", SearchView.as_view(), name="search"),
    path("search/results/", SearchResultsView.as_view(), name="search_results"),
    path("index/", IndexListView.as_view(), name="index"),
    path("contents/", ContentsListView.as_view(), name="contents"),
    path("sitenews/rss/", LatestPostsFeed(), name="post_feed"),
    path("sitenews/atom/", AtomLatestPostsFeed(), name="post_feed"),
    path("users/", include("users.urls", namespace="users")),
]
