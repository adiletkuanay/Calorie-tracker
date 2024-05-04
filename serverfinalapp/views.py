# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на ваш маршрут по умолчанию
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Маршрут по умолчанию после логина
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def home(request):
    if not request.user.is_authenticated:  # Проверяем, авторизован ли пользователь
        return redirect('login')  # Замените на ваш маршрут логина
    return render(request, 'home.html')
