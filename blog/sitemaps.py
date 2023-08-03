from django.contrib.sitemaps import Sitemap
from blog.models import post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
        return reverse('blog:detail',kwargs={'pk':item.id})