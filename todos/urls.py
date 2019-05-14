from django.urls import path
from todos.views import ListTodo, DetailTodo


urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]
