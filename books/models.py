from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=14)

    def __str__(self):
        return self.title
