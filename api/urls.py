from django.urls import path
from books.views import BookListView
from todos.views import ListTodo


urlpatterns = [
    path('books/', BookListView.as_view()),
    path('todos/', ListTodo.as_view()),
]
