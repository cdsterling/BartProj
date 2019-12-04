from django.shortcuts import render

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

def station_selected(request, stationID):
    #call the api using the station id
    # get the list of times
    # put the times into the context
    #return render(request, 'pages/station.html', context)