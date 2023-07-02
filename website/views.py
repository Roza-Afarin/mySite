from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

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
    #return HttpResponse('<h1>contact page</h1>')
    return render(request,'website/contact.html')