from django.contrib.sitemaps import Sitemap

from apps.blog.models import Category, Post


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Category.objects.all().prefetch_related('posts')


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=1).order_by('-publish_date')

    def lastmod(self, obj):
        return obj.updated_date
