from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils.timezone import now



class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True, published_date__lte=now())

    def lastmod(self, obj):
        return obj.published_date