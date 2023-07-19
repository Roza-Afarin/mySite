from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from blog.models import post
from django.views.generic import DetailView
import datetime

class PostDetailView(DetailView):
    model = post
    count_hit = True
    template_name = 'blog/blog-single.html'

def blog_index(request):
    posts = post.objects.filter(status = 1)
    now = datetime.datetime.now(datetime.timezone.utc)
    #posts = post.objects.filter(status = 1)
    context = {'posts':posts,'now':now}
    return render(request,'blog/blog-home.html',context)#template

#def blog_single(request):
#    posts = post.objects.filter(status = 1)
#    now = datetime.datetime.now(datetime.timezone.utc)
    #posts = post.objects.filter(status = 1)
#    context = {'posts':posts}
#    return render(request,'blog/blog-single.html')

def blog_test(request):
    posts = post.objects.filter(status = 1)
    now = datetime.datetime.now(datetime.timezone.utc)
    #posts = post.objects.filter(status=1)
    context = {'posts':posts,'now':now}
    #context = {'name':name,'family_name':family_name,'age':age}
    return render(request,'test.html',context)

