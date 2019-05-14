from blog.views import PostList, PostDetail
from django.urls import path


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
