from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    products = Product.objects.all()
    search = request.GET.get('search', '')
    category_name = request.GET.get('category', '')

    if search:
        products = products.filter(name__icontains=search)

    if category_name:
        products = products.filter(category__name=category_name)

    context = {
        'products': products,
        'search': search,
        'category_name': category_name,
        'categories': Category.objects.all()
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

def category(request, category_name):
    products = Product.objects.filter(category__name=category_name)

    context = {
        'products': products,
        'category_name': category_name
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')