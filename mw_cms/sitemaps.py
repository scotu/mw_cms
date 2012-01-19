from django.contrib.sitemaps import Sitemap
from treepages.models import Page

class SitoSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.active()

    def lastmod(self, obj):
        return obj.modified
