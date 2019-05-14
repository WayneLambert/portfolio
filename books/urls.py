from django.urls import path
from books.views import BookListView


urlpatterns = [
    path('', BookListView.as_view()),
]
