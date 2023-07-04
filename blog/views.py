from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def blog_index(request):
    return render(request,'blog/blog-home.html')#template

def blog_single(request):
    return render(request,'blog/blog-single.html')

