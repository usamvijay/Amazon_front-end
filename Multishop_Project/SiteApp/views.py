from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Site/index.html")

def cart_page(request):
    return render(request, "Site/cart.html")

def checkout_page(request):
    return render(request, "Site/checkout.html")
