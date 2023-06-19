from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:productId>', product, name='product')
]