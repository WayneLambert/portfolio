from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import ObjectDoesNotExist
from django.urls import reverse


class Profile(models.Model):

    class AuthorView(models.IntegerChoices):
        USERNAME = 0
        FULL_NAME = 1

    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    author_view = models.IntegerField(choices=AuthorView.choices, default=0)
    profile_picture = models.ImageField(
        default='default-user.jpg', upload_to='profile_pics', max_length=200)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"

    def get_absolute_url(self):
        return reverse('blog:users:profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify(self.full_name)

        _slug = self.slug
        _count = 1

        while True:
            try:
                Profile.objects.all().exclude(pk=self.pk).get(slug=_slug)
            except MultipleObjectsReturned:
                pass
            except ObjectDoesNotExist:
                break
            _slug = f"{self.slug}{_count}"
            _count += 1

        self.slug = _slug

        super(Profile, self).save(*args, **kwargs)
