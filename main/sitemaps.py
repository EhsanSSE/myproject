from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["main:index", "main:about", "main:contact", "blog:index"]

    def location(self, item):
        return reverse(item)