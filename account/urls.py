from django.contrib import admin
from django.urls import path
from account.views import ResetPasswordView
from django.contrib.auth import views as auth_views
###
from . import views
app_name = 'account'

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup_view,name='signup'),
     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
         path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

]