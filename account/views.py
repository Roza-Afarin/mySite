from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from account.forms import CustomUserCreationForm


# Create your views here.

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('account:login')


def login_view(request):
    '''
    if request.user.is_authenticated:
        msg = f'user is authonticated as {request.user.username}'
    else:
        msg = 'user is not authenticate'
    return render(request,'account/login.html',{'msg':msg})
    '''
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    pass
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'account/login.html',context)
    else:
        return redirect('/')

@login_required()
def logout_view(request):
    #if request.user.is_authenticated:
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        form = CustomUserCreationForm()
        content = {'form':form}
        return render(request,'account/signup.html',content)
    else:
        return redirect('/')

