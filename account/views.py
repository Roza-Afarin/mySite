from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

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
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        form = UserCreationForm()
        content = {'form':form}
        return render(request,'account/signup.html',content)
    else:
        return redirect('/')
