from django.contrib.auth.models import User
from django.db import models
from os import path
from ab_back_end.settings import BASE_DIR


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        default=path.join(BASE_DIR, 'ab_back_end/static/images/default.jpg'),
        upload_to='ab_back_end/static/profile_pics',
        )

    def __str__(self):
        return self.title
