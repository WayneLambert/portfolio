from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Profile(models.Model):

    class AuthorView(models.IntegerChoices):
        USERNAME = 0
        FULL_NAME = 1

    user = models.OneToOneField(
        get_user_model(), primary_key=True, related_name='user', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    author_view = models.IntegerField(choices=AuthorView.choices, default=0)
    profile_picture = models.ImageField(
        default='default-user.jpg', upload_to='profile_pics', max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"

    @property
    def initials(self):
        inits = f"{self.user.first_name[0]}{self.user.last_name[0]}"
        return inits.upper().strip()

    @property
    def join_year(self) -> int:
        return self.user.date_joined.year

    @property
    def display_name(self):
        if self.author_view == 0:
            return self.user.username
        else:
            return self.full_name

    def get_absolute_url(self):
        return reverse('blog:users:profile', kwargs={'username': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
