from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from products.models import Customer
from django.contrib import messages

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer(user=user)
            customer.save()
            messages.success(request,"Registration successful. You can now log in.")
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
            messages.success(request, 'Login Successfully')
            return redirect('index')
        else:
            logout(request)
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    
    return render(request, 'login.html')


def userLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('index')