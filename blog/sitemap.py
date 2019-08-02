from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Category, Post


class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1).order_by('-publish_date')

    def lastmod(self, obj):
        return obj.updated_date
