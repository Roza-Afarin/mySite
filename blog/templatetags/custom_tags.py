from django import template
from blog.models import post,Category,Comment

register = template.Library()

@register.simple_tag(name='comment_count')
def count_comments(pid):
    posts = post.objects.get(id=pid)
    return Comment.objects.filter(post=posts).count()

@register.simple_tag
def subtract(value, arg):
    return value - arg

#register.filter('subtract', subtract)

@register.simple_tag(name='countP')
def count_null_previous_status(previous):
    posts = post.objects.all().order_by('id')
    count = 0
    try:
        while not previous.status:
            count+=1
            previous = post.objects.get(id=(previous.id)-1)
        return count
    except previous.DoesNotExist:
        previous = None
        count = 0
        return count

@register.simple_tag(name='countN')
def count_null_next_status(next):
    posts = post.objects.all().order_by('id')
    count = 0
    try: 
        while not next.status:
            count+=1
            next = post.objects.get(id=(next.id)+1)
        return count
    except next.DoesNotExist:
        next = None
        count = 0
        return count
    
@register.inclusion_tag('blog/latest-posts.html')
def latestposts(arg=2):
    posts = post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/post-cat.html')
def postcategories():
    posts = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
        return {'cat':cat_dict}
