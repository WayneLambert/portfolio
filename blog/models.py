from os import path
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ab_back_end.settings import BASE_DIR


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/category/' & self.slug


class Post(models.Model):
    STATUS = (
        (0, 'Draft'),
        (1, 'Publish')
    )
    title = models.CharField(max_length=65)
    slug = models.SlugField(max_length=65, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        default=path.join(BASE_DIR, 'ab_back_end/static/images/default.png'),
        upload_to='ab_back_end/static/profile_pics',
    )
    categories = models.ManyToManyField(Category, blank=True, related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
