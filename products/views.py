from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def product(request, productId):
    products = Product.objects.all()
    product = Product.objects.filter(id = productId)
    
    context = {
        'product': product,
        'products': products
    }
    
    return render(request, 'productdetail.html', context)