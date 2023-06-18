from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginAndRegister')
        
    context = {
        'form' : form
    }
    return render(request, 'loginAndRegister.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            logout(request)
            return redirect('loginAndRegister')
        