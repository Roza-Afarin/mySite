from django.shortcuts import render,get_object_or_404

# Create your views here.
#from django.http import HttpResponse,JsonResponse
from blog.models import post
import datetime
from hitcount.views import HitCountDetailView

class PostDetailView(HitCountDetailView):
    model = post
    count_hit = True
    template_name = 'blog/blog-single.html'

    

def blog_index(request):
    posts = post.objects.filter(published_date__lte = datetime.datetime.now(datetime.timezone.utc))
    #now = datetime.datetime.now(datetime.timezone.utc)
    #posts = post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)#template

def blog_single(request,pk):
    posts = get_object_or_404(post,pk=pk,status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-single.html',context)

def blog_test(request):
    posts = post.objects.filter(status = 1)
    now = datetime.datetime.now(datetime.timezone.utc)
    #posts = post.objects.filter(status=1)
    context = {'posts':posts,'now':now}
    #context = {'name':name,'family_name':family_name,'age':age}
    return render(request,'test.html',context)

