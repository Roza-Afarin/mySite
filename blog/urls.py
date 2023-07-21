from django.contrib import admin
from django.urls import path
###
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('<int:pk>',blog_single,name='detail'),
    path('test',blog_test,name='test'),
    #path('blog/<int:pk>/<str:slug>/', PostDetailView.as_view(),   name='post')
    #path('blog/blog/<int:pk>/<str:slug>/', PostDetailView.as_view(),   name='detail')
]
