from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed

from .models import Post


class LatestPostsFeed(Feed):
    title = "Wayne Lambert | Blog"
    link = "/blog/sitenews/"
    description = "Latest posts from Wayne Lambert's Blog"

    def items(self):
        return Post.objects.filter(status=1).order_by('-publish_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_author_name(self, item):
        return item.author.user.full_name

    def item_updateddate(self, item):
        return item.updated_date


class AtomLatestPostsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description
