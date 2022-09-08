from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
                # Display some error
                pass

    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            return redirect(reverse('dashboard'))

    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})