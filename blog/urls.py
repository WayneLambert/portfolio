from django.contrib import admin
from django.urls import include, path
from .views import PostList, PostDetail


urlpatterns = [
    path('blog', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
