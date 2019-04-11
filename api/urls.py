from django.urls import path
from books.views import BookListView
from todos.views import ListTodo
from blog.views import PostList, PostDetail


urlpatterns = [
    path('books/', BookListView.as_view()),
    path('todos/', ListTodo.as_view()),
    path('blog/', PostList.as_view()),
]
