from django.shortcuts import render,get_object_or_404

# Create your views here.
#from django.http import HttpResponse,JsonResponse
#import datetime
#from hitcount.views import HitCountDetailView
#from django.core.paginator import Paginator
from blog.models import post
from datetime import *
from django.utils import timezone
from django.views.generic import ListView


#class PostDetailView(HitCountDetailView):
#    model = post
#    count_hit = True
#    template_name = 'blog/blog-single.html'

#def blog_test(request):
#    posts = post.objects.filter(status = 1)
#    now = datetime.datetime.now(datetime.timezone.utc)
#    #posts = post.objects.filter(status=1)
#    context = {'posts':posts,'now':now}
#    context = {'name':name,'family_name':family_name,'age':age}
#    return render(request,'test.html',context)   

class PostListView(ListView):
    model = post
#    template_name = 'blog/blog-single.html'
    paginate_by = 1
#    queryset = post.objects.order_by('-id')
    


def blog_index(request,**kwargs):
    posts = post.objects.filter(published_date__lte=timezone.now(),status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    #now = datetime.datetime.now(datetime.timezone.utc)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)#template

def blog_single(request,pk):
    posts = get_object_or_404(post,pk=pk,status = 1)
    posts.conted_vies+=1
    posts.save()
    #paging = post.objects.all().order_by('id')
    #paginator = Paginator(paging, 1)
    #page_number = request.GET.get("page")
    #page_obj = paginator.get_page(page_number)
    #context = {'posts':posts,"page_obj": page_obj}
    try:
        next = posts.get_next_by_created_date()
    except posts.DoesNotExist:
        next = None
    try:
        previous = posts.get_previous_by_created_date()
    except posts.DoesNotExist:
         previous = None
    context = {'posts':posts,'next':next,'previous':previous}
    return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts = post.objects.filter(status=1,category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = post.objects.filter(published_date__lte=timezone.now(),status = 1)
    if request.method=='GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)#template