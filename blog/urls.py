from django.contrib import admin
from django.urls import path
###
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('single',blog_single,name='detail'),
    path('<str:name>/<str:family_name>/<str:age>',blog_test,name='test')
]
