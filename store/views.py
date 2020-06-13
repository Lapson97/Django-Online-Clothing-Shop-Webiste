from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    return render(request, "store/store.html")

def login_page(request):
    return render(request, "store/login.html")

def register_page(request):
    return render(request, "store/register.html")

def clothes(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "store/clothes.html", context)

def clothes_detail(request, pk):
    product = Product.objects.get(id=pk)
    choices = product.clothing_size.all()
    context = {
        'product': product,
        'choices': choices
    }
    return render(request, "store/clothesdetail.html", context)

def shoes(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "store/shoes.html", context)

def shoes_detail(request, pk):
    product = Product.objects.get(id=pk)
    choices = product.shoe_size.all()
    context = {
        'product': product,
        'choices': choices
    }
    return render(request, "store/clothesdetail.html", context)

def accessories(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "store/accessories.html", context)

def accessories_detail(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,

    }
    return render(request, "store/accessoriesdetail.html", context)

def checkout(request):
    return render(request, "store/checkout.html")