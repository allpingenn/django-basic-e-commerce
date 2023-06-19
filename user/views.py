from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

def userRegister(request):
    form = UserForm()
    button = True
    baslik = True
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            button = False
            baslik = False
            return redirect('login')
        
    context = {
        'form': form,
        'button': button,
        'baslik': baslik,
    }
    return render(request, 'loginAndRegister.html', context)

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
    
    return render(request, 'loginAndRegister.html')

def userLogout(request):
    logout(request)
    return redirect('index')