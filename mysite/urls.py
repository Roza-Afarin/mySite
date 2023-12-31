"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
###
from django.conf import settings
from django.conf.urls.static import static
#from website.views import http_test, json_test
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.urls import re_path
from django.conf import settings
from . import veiws


sitemaps = {
    "static": StaticViewSitemap,
    'blog': BlogSitemap,
}
if settings.MAINTENANCE_MODE:
    urlpatterns = [
        re_path(r'.*', veiws.maintenance)
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        ####
        ##path('urlAdd','view')
        #path('website/',include('website.urls'))
        path('',include('website.urls')),# home page
        path('blog/',include('blog.urls')),
        path('account/',include('account.urls')),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
        path('robots.txt', include('robots.urls')),
        path("__debug__/", include("debug_toolbar.urls")),
        path('summernote/', include('django_summernote.urls')),
        path('captcha/', include('captcha.urls')),
    ]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

