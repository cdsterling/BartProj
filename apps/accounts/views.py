from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import FavoriteStationForm, SignupForm
from apps.accounts.models import FavoriteStation
from django.contrib.auth.models import User
from apps.core import bart

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
    return redirect('') 


@login_required
def favorites(request):
    if request.method == 'POST':
        print("method is a post")
        form = FavoriteStationForm(request.POST)
        print(type(form))
        if form.is_valid():
            station = form.save(commit=False)
            if not FavoriteStation.objects.filter(
                user_id=request.user,
                station=station.station, 
            ):
                print('save station')
                station.user = request.user
                station.save()

    else:
        form = FavoriteStationForm(instance=request.user)

    # filters for favorited stations by user
    favorite_stations = FavoriteStation.objects.filter(user=request.user).order_by('station')

    context = {
        'form': form,
        'favorite_stations': favorite_stations, 
    }
    return render(request, 'accounts/favorites.html', context)

def remove_favorite(request, station_abbr): 
    station = FavoriteStation.objects.filter(
        user_id=request.user.id,
        station=station_abbr, 
        )
    station.delete()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))