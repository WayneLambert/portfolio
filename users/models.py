from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg',
                                        upload_to='profile_pics'
                                        )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        image = Image.open(self.profile_picture.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save()
