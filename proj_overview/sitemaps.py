from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import ArticleInfo

class ArticleSitemap(Sitemap):
    def items(self):
        return ArticleInfo.objects.all()
    
    def location(self, item):
        return reverse('proj_overview:detail', args=[item.id])
