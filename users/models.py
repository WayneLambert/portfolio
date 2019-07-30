from django.contrib.auth.models import User
from django.db import models
import os
from PIL import Image
from ab_back_end.settings import DEFAULT_IMAGES_ROOT


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

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.user.username})'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.profile_picture.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_picture.path)
