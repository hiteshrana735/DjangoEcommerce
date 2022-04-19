from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def store(request):
    products = Product.objects.all()
    context ={'products' : products}
    return render(request, 'store.html', context)

def cart(request):
    context ={}
    return render(request, 'cart.html', context)

def checkout(request):
    context ={}
    return render(request, 'checkout.html', context)