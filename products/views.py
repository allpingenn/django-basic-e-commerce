from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    products = Product.objects.all()
    
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        products = Product.objects.filter(name__icontains = search)
    
    context = {
        'products': products,
        'search': search
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

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')