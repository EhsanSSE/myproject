from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils.timezone import now



class LatestEntriesFeed(Feed):
    title = "Blog Posts"
    link = "/blog/"
    description = "Got Some Information About Fly And Pilot."

    def items(self):
        return Post.objects.filter(status=True, published_date__lte=now())

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
