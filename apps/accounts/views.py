from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import FavoriteForm, SignupForm
from apps.accounts.models import User, FavoriteStations

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('') #might want to change this redirect to '' to send to homepage?


@login_required
def favorites(request):
    if request.method == 'POST':
        form = FavoriteForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FavoriteForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/favorites.html', context)


