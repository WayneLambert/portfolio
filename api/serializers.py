from rest_framework import serializers
from books.models import Book
from todos.models import Todo


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'user',
            'title',
            'description',
            'open_date',
            'updated_date',
            'due_date',
            'completed_date',
            'draft',
            'priority',
            'project',
            'owner',
        )
