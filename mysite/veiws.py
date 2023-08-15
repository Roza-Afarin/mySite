from django.http import HttpResponse
def maintenance(request):
    return HttpResponse('<h1>به زودی در دسترس خواهد بود</h1>')