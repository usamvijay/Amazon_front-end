
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from SiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('site/', include('SiteApp.urls')),
    path('dashboard/', include('AdminApp.urls')),
]
