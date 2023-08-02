from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsletterForm
from website.models import contact
from django.contrib import messages

#def _test(request):
#    return HttpResponse('<h1>HTTP response</h1>')

#def json_test(request):
#    return JsonResponse({'name':'roza','family':'afarin'})
def home_index(request):
    #return HttpResponse('<h1>home page</h1>')
    return render(request,'website/index.html')

def about_index(request):
    #return HttpResponse('<h1>about page</h1>')
    return render(request,'website/about.html')

def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = 'unknown'
            form = form.save()
            messages.add_message(request, messages.SUCCESS, "your ticket submitted successfully")
        else:
            messages.add_message(request, messages.ERROR, "your ticket didn't submitted")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newletter_index(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "your email addr submitted successfully")
        else:
            messages.add_message(request, messages.ERROR, "your email addr didn't submitted")
    return HttpResponseRedirect('/')
