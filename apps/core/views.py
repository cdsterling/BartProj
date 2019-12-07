from django.shortcuts import render
from . import bart 

# Two example views. Change or delete as necessary.
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

# def show_station(request, stationID):
def show_station(request, stn_abbr):
    
    #call the api using the station id
    arrivals = bart.station_arrivals(stn_abbr)
    # print("printing arrivals", arrivals)

    all_stations = bart.stations()
    print("-----------showing station", stn_abbr)

    station_name=''
    for single_station in all_stations:
        if stn_abbr == single_station['abbr']:
            station_name = single_station['name']
            break

    print('arrival keys', arrivals.keys())   
    # for train in arrivals[stn_abbr]:
    #     print("update datetime", train["update_datetime"])
    #     print("station Name", train["station_name"])
    #     print("destination name", train["destination_name"])
    #     print("Arrival minutes", train["arrival_minutes"])
    #     print("color", train["color"])
    #     print("------------------------------------")     
    context = {
        'arrivals': arrivals[stn_abbr],
        'station_name' : station_name

    }
    return render(request, 'pages/station_list.html', context)