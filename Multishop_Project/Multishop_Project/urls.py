
from django.contrib import admin
from django.urls import path
from SiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('cart/',views.cart_page),
    path('checkout/',views.checkout_page),
]
