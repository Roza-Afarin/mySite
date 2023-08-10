from django.contrib import admin
from django.urls import path
###
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('<int:pk>',blog_single,name='detail'),
    path('category/<str:cat_name>',blog_index,name='category'),
    path('author/<str:author_username>',blog_index,name='author'),
    path('tag/<str:tag_name>',blog_index,name='tag'),
    path('search/',blog_search,name='search'),
   
    #path('blog/<int:pk>',PostListView.as_view()),
    #path('test',blog_test,name='test'),
    #path('blog/<int:pk>/<str:slug>/', PostDetailView.as_view(),   name='post')
    #path('blog/blog/<int:pk>/<str:slug>/', PostDetailView.as_view(),   name='detail')
]
