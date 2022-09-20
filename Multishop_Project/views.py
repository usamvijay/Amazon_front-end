from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Site/index.html")

def cart_page(request):
    return render(request, "Site/cart.html")

def checkout_page(request):
    return render(request, "Site/checkout.html")

def Shop_page(request):
    return render(request, "Site/shop.html")

def Shop_details_page(request):
    return render(request, "Site/shop_detail.html")

def Contact_Us_page(request):
    return render(request, "Site/contact.html")

def Register_page(request):
    return render(request, "Site/Register.html")
