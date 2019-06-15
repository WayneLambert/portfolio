from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from os import path
from ab_back_end.settings import BASE_DIR


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        default=path.join(BASE_DIR, 'ab_back_end/static/images/default.jpg'),
        upload_to='ab_back_end/static/profile_pics',
    )
    categories = models.ManyToManyField('Category', related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
