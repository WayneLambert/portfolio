from django.urls import path, include
from books.views import BookListView
from todos.views import ListTodo
from blog.views import PostList, PostDetail
from analytics.views import AnalyticsViewSet


urlpatterns = [
    path('books/', BookListView.as_view()),
    path('todos/', ListTodo.as_view()),
    path('blog/', PostList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('analytics/', AnalyticsViewSet.as_view(actions={'get': 'list'})),
]
