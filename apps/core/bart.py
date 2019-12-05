import requests
import os
from datetime import datetime, timedelta
import pprint
bart_key = os.getenv("BART_API_KEY")

# BART API 
def station_arrivals(): 
    """
    KEY DEFINITIONS
    station_name - station where train is arriving
    station_abbr - abbreviated station name where train is arriving
    destination_name - final destination of train
    destination_abbr - abbreviated final destination of train
    arrival_minutes - minutes until train arrives
    arrival_datetime - arrival time of the train
    """


    params = {'key': bart_key, 'cmd': 'etd', 'orig': 'ALL', 'json': 'y'}
    response = requests.get('http://api.bart.gov/api/etd.aspx', params=params)
    print(f'Request status code: {response.status_code}')
    result = response.json()['root']

    update_datetime = datetime.combine(
        datetime.strptime(result['date'], "%m/%d/%Y"),
        datetime.strptime(result['time'],"%I:%M:%S %p %Z").time()
    )
    arrivals = {}
    for station in result['station']: 
        arrivals[station['abbr']] = []
        for destination in station['etd']: 
            for train in destination['estimate']: 
                arrivals[station['abbr']].append({
                    'update_datetime': update_datetime,
                    'station_name': station['name'],
                    'station_abbr': station['abbr'],
                    'destination_name': destination['destination'],
                    'destination_abbr': destination['abbreviation'],
                    'arrival_minutes': train['minutes'],
                    'arrival_datetime': estimate_arrival(update_datetime, train['minutes']), 
                    'platform': train['platform'],
                    'direction': train['direction'],
                    'length': train['length'],
                    'color': train['color'],
                    'hexcolor': train['hexcolor'], 
                    'bikeflag': train['bikeflag'],
                    'delay_seconds': train['delay'],   
                })
    return arrivals

def estimate_arrival(update_datetime, arrival_minutes): 
    try: 
        arrival = int(arrival_minutes)
    except ValueError: 
        arrival = 0
    return update_datetime + timedelta(minutes=arrival)

def main(): 
    arrivals = station_arrivals()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(arrivals)


if __name__ == '__main__': 
    main()