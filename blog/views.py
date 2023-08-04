from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
#from django.http import HttpResponse,JsonResponse
#import datetime
#from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import post,Comment
from datetime import *
from django.utils import timezone
from django.views.generic import ListView
from blog.forms import CommentsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    #paging = post.objects.all().order_by('id')
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    #now = datetime.datetime.now(datetime.timezone.utc)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)#template

def blog_single(request,pk):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.SUCCESS, "your comment submitted successfully")
        else:
            messages.add_message(request, messages.ERROR, "your comment didn't submitted")
    
    posts = get_object_or_404(post,pk=pk,status = 1)
    posts.conted_vies+=1
    posts.save()
    try:
        next = posts.get_next_by_created_date()
    except posts.DoesNotExist:
        next = None
    try:
        previous = posts.get_previous_by_created_date()
    except posts.DoesNotExist:
        previous = None
    if not posts.login_requier:
        comments = Comment.objects.filter(post=posts.id,approved=True).order_by('-created_date')
        form = CommentsForm()
        context = {'posts':posts,'next':next,'previous':previous,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return redirect('/account/login')

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

