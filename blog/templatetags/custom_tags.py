from django import template
from blog.models import post

register = template.Library()

@register.simple_tag
def subtract(value, arg):
    return value - arg

#register.filter('subtract', subtract)

@register.simple_tag(name='countP')
def count_null_previous_status(previous):
    count = 0
    while not previous.status:
        count+=1
        previous = post.objects.get(id=(previous.id)-1)
    return count

@register.simple_tag(name='countN')
def count_null_next_status(next):
    count = 0
    while not next.status:
        count+=1
        next = post.objects.get(id=(next.id)+1)
    return count

