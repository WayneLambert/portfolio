import os
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse
from PIL import Image
from ab_back_end.settings import DEFAULT_IMAGES_ROOT


class Category(models.Model):
    name = models.CharField(max_length=16)
    slug = models.SlugField(max_length=16, unique=True)
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
    slug = models.SlugField(
        max_length=65,
        unique=True,
        help_text="""
        The slug can be any words you like separated by dashes.
        Prepositions and pronouns are unncessary from an SEO perspective.
        """,
    )
    content = RichTextUploadingField()
    reference_url = models.URLField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        default=os.path.join(DEFAULT_IMAGES_ROOT, 'default-post.jpg'),
        upload_to='ab_back_end/static/post_images',
        max_length=200,
    )
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, related_name='posts')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 120 or img.width > 120:
            output_size = (120, 120)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
