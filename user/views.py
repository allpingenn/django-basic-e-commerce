from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from products.models import Customer

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer(user=user)
            customer.save()
            return redirect('login')
        
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            logout(request)
            return redirect('login')
    
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('index')