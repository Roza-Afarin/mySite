from django.contrib import admin
from django.urls import path
###
from website.views import *

urlpatterns = [
    #path('urlAdd','view')
    #path('home',home_index),
    path('',home_index),
    path('about',about_index),
    path('contact',contact_index)
]
