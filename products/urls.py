from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:productId>', product, name='product'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('category/<str:category_name>/', category, name='category'),
    path('update_item/', updateItem, name='update_item'),
    path('delete_item/', deleteItem, name='delete_item'),
    path('wishlist/', wishlist, name='wishlist'),
    path("update_wishlist_item/", updateWishlist, name="updateWishlist"),
    path('delete_wishlist_item/', deleteWishlistItem, name='deleteWishlistItem'),
]