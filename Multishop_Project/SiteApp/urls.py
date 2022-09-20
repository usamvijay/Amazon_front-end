
from django.contrib import admin
from django.urls import path
from SiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('cart/',views.cart_page),
    path('checkout/',views.checkout_page),
    path('shop/',views.Shop_page),
    path('shop_details/',views.Shop_details_page),
    path('Contact_Us/',views.Contact_Us_page),
    path('Register/',views.Register_page),
]
