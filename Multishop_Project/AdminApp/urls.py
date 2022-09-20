
from django.contrib import admin
from django.urls import path
from AdminApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard/', views.Dashboard),
   
]
