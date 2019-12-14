from django.shortcuts import render
from . import bart 
from django.contrib.auth.decorators import login_required
from apps.accounts.models import FavoriteStation
from django.contrib.auth.models import User


# Two example views. Change or delete as necessary.
def homepage(request):
    context = {
        'example_context_variable': 'Change me.',
    }
    return render(request, 'pages/home_logged_out.html', context)

def home(request):
    context = {
        'example_context_variable': 'Change me.',
    }
    return render(request, 'pages/home_logged_in.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def faq(request):
    context = {

    }

    return render(request, 'pages/faq.html', context)

def homepage_logged_out(request, stn_abbr="SELECT"):
    
    station_list = [(station['abbr'], station['name']) for station in bart.stations()]
    arrivals = {}
    station_name=''

    arrivals = get_arrivals_for_station(stn_abbr)
    station_name = get_station_name_for_abbr(stn_abbr)        
    # print("arrivals", arrivals)
    print("Station name:", station_name)
    context = {
        'station_list': station_list,
        'arrivals': arrivals,
        'station_name' : station_name

    }
    return render(request, 'pages/home_logged_out.html', context)

def get_arrivals_for_station(stn_abbr):
    if stn_abbr != "SELECT" and stn_abbr != "":
        #call the api using the station id
        arrivals = bart.station_arrivals(stn_abbr)[stn_abbr]
        return arrivals

def get_station_name_for_abbr(stn_abbr):
    #get the full name of the station from bart.stations - 
    # eventually we want that info in the Database
    all_stations = bart.stations()
    station_name=''
    for single_station in all_stations:
        if stn_abbr == single_station['abbr']:
            return single_station['name']



@login_required
def homepage_logged_in(request):

    print("Chad1")
    all_station_list = [(station['abbr'], station['name']) for station in bart.stations()]

    # filters for favorited stations by user
    favorite_stations = FavoriteStation.objects.filter(user=request.user)

    print("Favorite Stations:", favorite_stations)

    arrivals = []
    station_names = []
    all_stations = bart.stations()

    # for each preferred_station in user preferences:
    for station in favorite_stations:
        print("station:", station.station)
        arrivals.append(get_arrivals_for_station(station.station))
        station_names.append(get_station_name_for_abbr(station.station))
        
    station_names_and_arrivals = zip(station_names, arrivals)

    print("station names and arrivals", station_names_and_arrivals)
    context = {
        "station_names_and_arrivals": station_names_and_arrivals,
        "station_list" : all_station_list,
        
    }
    return render(request, 'pages/home_logged_in.html', context)

