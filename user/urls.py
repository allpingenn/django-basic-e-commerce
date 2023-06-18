from django.urls import path
from .views import *

urlpatterns = [
    path('loginAndRegister/', userRegister, name='loginAndRegister'),
    path('loginAndRegister/', userLogin, name='loginAndRegister'),
]