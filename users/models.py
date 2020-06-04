from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    AUTHOR_VIEW = (
        (0, 'Username'),
        (1, 'Full Name')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='default-user.jpg',
        upload_to='profile_pics',
        max_length=200,
    )
    author_view = models.IntegerField(choices=AUTHOR_VIEW, default=0)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.user.username})'
