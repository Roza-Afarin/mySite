from django import template
from blog.models import post

register = template.Library()

@register.inclusion_tag('website/home-latest-posts.html')
def latest_posts(arg=6):
    posts = post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}