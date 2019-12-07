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
    print("-----------showing station")
    #call the api using the station id
    arrivals = bart.station_arrivals(stn_abbr)
    # print("printing arrivals", arrivals)

    print(arrivals.keys())   
    # for train in arrivals[stn_abbr]:
    #     print("update datetime", train["update_datetime"])
    #     print("station Name", train["station_name"])
    #     print("destination name", train["destination_name"])
    #     print("Arrival minutes", train["arrival_minutes"])
    #     print("color", train["color"])
    #     print("------------------------------------")     
    context = {
        'arrivals': arrivals[stn_abbr],
        'station_name' : arrivals[stn_abbr][0]["station_name"]

    }
    return render(request, 'pages/station_list.html', context)