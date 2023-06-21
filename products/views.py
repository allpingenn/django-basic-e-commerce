from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.

def index(request):
    products = Product.objects.all()
    search = request.GET.get('search', '')
    category_name = request.GET.get('category', '')
    customer = None
    cartItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items

    if search:
        products = products.filter(name__icontains=search)

    if category_name:
        products = products.filter(category__name=category_name)

    context = {
        'products': products,
        'search': search,
        'category_name': category_name,
        'categories': Category.objects.all(),
        'cartItems': cartItems,
    }

    return render(request, 'index.html', context)




def product(request, productId):
    products = Product.objects.all()
    product = Product.objects.get(id=int(productId))
    customer = None
    cartItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if not created:
            cartItems = order.get_cart_items
    
    context = {
        'product': product,
        'products': products,
        'cartItems': cartItems
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
    customer = None
    cartItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if not created:
            cartItems = order.get_cart_items
    
    context = {
        'cartItems': cartItems
    }
    
    return render(request, 'contact.html', context)


def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'fullTotal':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems
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
        if orderItem.quantity > 1:
            orderItem.quantity = (orderItem.quantity -1)
        
    orderItem.save()

    return JsonResponse('Item was updated', safe=False)

def deleteItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem = OrderItem.objects.filter(order=order, product=product)
    
    if orderItem.exists():
        orderItem.delete()
        order = Order.objects.get(id=order.id)
        order.save()

        return JsonResponse('Item was deleted', safe=False)
    else:
        return JsonResponse('Item not found', safe=False)
