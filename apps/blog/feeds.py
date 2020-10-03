from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed, Enclosure

from apps.blog.models import Post


class LatestPostsFeed(Feed):
    title = "Wayne Lambert"
    link = "/blog/sitenews/"
    description = "Latest posts from Wayne Lambert's Blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_author_name(self, item):
        return item.author.user.full_name

    def item_pubdate(self, item):
        return item.publish_date

    def item_updateddate(self, item):
        return item.updated_date

    def item_enclosures(self, item):
        return [Enclosure(
            item.image.url,
            str(item.image.size),
            f"image/{item.image.name.split('.')[-1]}"
        )]


class AtomLatestPostsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description
