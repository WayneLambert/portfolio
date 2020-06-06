from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostsFeed(Feed):
    title = "Wayne Lambert | Blog"
    link = "/sitenews/"
    description = "Latest posts from Wayne Lambert's Blog"

    def items(self):
        return Post.objects.filter(status=1).order_by('-publish_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
