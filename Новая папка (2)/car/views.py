from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Car


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'car/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'car/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    cars = Car.objects.all()
    return render(request, 'car/dashboard.html', {'cars': cars})


@login_required(login_url='login')
def dashboard(request):
    cars = Car.objects.all()
    return render(request, 'car/dashboard.html', {'cars': cars})

