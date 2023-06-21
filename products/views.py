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
    wishlistItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
        wishlistItems = wishlist.get_wishlist_items

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
        'wishlistItems': wishlistItems,
    }

    return render(request, 'index.html', context)




def product(request, productId):
    products = Product.objects.all()
    product = Product.objects.get(id=int(productId))
    customer = None
    cartItems = 0
    wishlistItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
        wishlistItems = wishlist.get_wishlist_items
    
    context = {
        'product': product,
        'products': products,
        'wishlistItems': wishlistItems,
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
    wishlistItems = 0

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
        wishlistItems = wishlist.get_wishlist_items
    
    context = {
        'cartItems': cartItems,
        'wishlistItems': wishlistItems,
    }
    
    return render(request, 'contact.html', context)


def cart(request):
    
    customer = None
    cartItems = 0
    wishlistItems = 0
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
        wishlistItems = wishlist.get_wishlist_items
    else:
        items = []
        order = {'get_cart_total':0, 'fullTotal':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems,
        'wishlistItems': wishlistItems,
    }
    
    return render(request, 'cart.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

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

def wishlist(request):
    
    customer = None
    cartItems = 0
    wishlistItems = 0
    
    if request.user.is_authenticated:
        customer = request.user.customer
        wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
        wishlist_items = wishlist.wishlistitem_set.all()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        wishlistItems = wishlist.get_wishlist_items
    else:
        wishlist_items = []
        
    context = {
        'wishlist_items': wishlist_items,
        'cartItems': cartItems,
        'wishlistItems': wishlistItems,
    }
    
    return render(request, 'wishlist.html',context)

def updateWishlist(request):
    data = json.loads(request.body)
    productId = data['productId']
    customer = request.user.customer
    product = Product.objects.get(id=int(productId))
    wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
    
    wishlistItem, created = WishlistItem.objects.get_or_create(wishlist = wishlist, product = product)
    wishlistItem.quantity = 1
        
    wishlistItem.save()

    return JsonResponse('Item was updated', safe=False)

def deleteWishlistItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    wishlist, created = Wishlist.objects.get_or_create(customer=customer, complete=False)
    
    wishlistItem = WishlistItem.objects.filter(wishlist=wishlist, product=product)
    
    if wishlistItem.exists():
        wishlistItem.delete()
        wishlist = Wishlist.objects.get(id=wishlist.id)
        wishlist.save()

        return JsonResponse('Item was deleted', safe=False)
    else:
        return JsonResponse('Item not found', safe=False)