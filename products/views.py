from django.shortcuts import render
from django.http import JsonResponse
import json
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
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'fullTotal':0}
        
    context = {
        'items': items,
        'order': order,
    }
    
    return render(request, 'cart.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
        
    orderItem.save()

    return JsonResponse('Item was updated', safe=False)

