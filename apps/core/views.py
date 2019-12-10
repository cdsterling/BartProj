from django.shortcuts import render
from . import bart 

# Two example views. Change or delete as necessary.
def homepage(request):
    context = {
        'example_context_variable': 'Change me.',
    }
    return render(request, 'pages/home.html', context)

def home(request):
    context = {
        'example_context_variable': 'Change me.',
    }
    return render(request, 'pages/home.html', context)

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


    if stn_abbr != "SELECT" and stn_abbr != "":
        #call the api using the station id
        arrivals = bart.station_arrivals(stn_abbr)[stn_abbr]

        #get the full name of the station from bart.stations - 
        # eventually we want that info in the Database
        all_stations = bart.stations()
        station_name=''
        for single_station in all_stations:
            if stn_abbr == single_station['abbr']:
                station_name = single_station['name']
                break

    print("arrivals", arrivals)

    context = {
        'station_list': station_list,
        'arrivals': arrivals,
        'station_name' : station_name

    }
    return render(request, 'pages/home_logged_out.html', context)

def homepage_logged_in(request):
    arrivals = []
    station_names = []
    all_stations = bart.stations()

    # for each preferred_station in user preferences:
        # arrivals.append(bart.station_arrivals(preferred_station))
        # for single_station in all_stations:
        # if preferred_station == single_station['abbr']:
        #     station_names.append(single_station['name'])
        #     break


    context = {
        "arrivals_list" : arrivals,
        "station_names": station_names
    }
    return render(request, 'pages/station_list.html', context)

