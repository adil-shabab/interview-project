from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'frontend/home.html')


    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'frontend/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'frontend/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  



def admin_home(request):
    return render(request, 'backend/home.html')

def admin_login(request):
    return render(request, 'backend/login.html')



def add_product(request):
    return render(request, 'backend/add-product.html')

