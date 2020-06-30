import math

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=16)
    slug = models.SlugField(max_length=16, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/category/' & self.slug


class Post(models.Model):
    STATUS = (
        (0, 'Draft'),
        (1, 'Publish')
    )
    title = models.CharField(
        max_length=60,
        validators=[MinLengthValidator(40)],
        help_text='The length of the post must be between 40 and 60 characters'
    )
    slug = models.SlugField(max_length=60, unique=True)
    content = RichTextUploadingField()
    reference_url = models.URLField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        default='default-post.jpg',
        upload_to='post_images',
        max_length=200,
        help_text='For bests results, use an image that is 1,200px wide x 600px high',
    )
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        help_text='Select more than one category by holding down Ctrl or Cmd key'
    )

    class Meta:
        ordering = ['-updated_date', '-publish_date']

    def __str__(self):
        return self.title

    @property
    def word_count(self) -> int:
        return len(self.content.split())

    @property
    def reading_time(self) -> int:
        return int(math.ceil(self.word_count / 75))

    def save(self):
        if not self.slug.strip():
            self.slug = slugify(self.title)

        _slug = self.slug
        _count = 1

        while True:
            try:
                Post.objects.all().exclude(pk=self.pk).get(slug=_slug)
            except MultipleObjectsReturned:
                pass
            except ObjectDoesNotExist:
                break
            _slug = f"{self.slug}{_count}"
            _count += 1

        self.slug = _slug

        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def get_excerpt(self, char):
        return self.content[:char]
