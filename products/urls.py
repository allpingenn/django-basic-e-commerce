from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:productId>', product, name='product'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
]