from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, RegisterForm

def log_in(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))

            else:
                messages.error(request, 'Las credenciales son inválidas')

    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))

    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('login'))