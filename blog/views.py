from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from blog.models import post

def blog_index(request):
    posts = post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)#template

def blog_single(request):
    return render(request,'blog/blog-single.html')

def blog_test(request,name,family_name,age):
    #posts = post.objects.all()
    #posts = post.objects.filter(status=1)
    #context = {'posts':posts}
    context = {'name':name,'family_name':family_name,'age':age}
    return render(request,'test.html',context)

