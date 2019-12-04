import requests
import os
from datetime import datetime, timedelta
from .models import StationArrival

# BART API 
def station_arrivals(): 
    params = {'key': bart_key, 'cmd': 'etd', 'orig': 'ALL', 'json': 'y'}
    response = requests.get('http://api.bart.gov/api/etd.aspx', params=params)
    print(f'Request status code: {response.status_code}')
    result = response.json()['root']

    update_datetime = datetime.combine(
        datetime.strptime(result['date'], "%m/%d/%Y"),
        datetime.strptime(result['time'][:7],"%I:%M:%S").time()
    )
    for station in result['station']: 
        for destination in station['etd']: 
            for train in destination['estimate']: 
                StationArrival.objects.create(
                    update_datetime=update_datetime,
                    station_name=station['name'],
                    station_abbr=station['abbr'],
                    destination_name=destination['destination'],
                    destination_abbr=destination['abbreviation'],
                    arrival_minutes=train['minutes'],
                    arrival_datetime=estimate_arrival(update_datetime, train['minutes']), 
                    platform=train['platform'],
                    direction=train['direction'],
                    length=train['length'],
                    color=train['color'],
                    hexcolor=train['hexcolor'], 
                    bikeflag=train['bikeflag'],
                    delay_seconds=train['delay'],
                )

def estimate_arrival(update_datetime, arrival_minutes): 
    try: 
        arrival = int(arrival_minutes)
    except ValueError: 
        arrival = 0
    return update_datetime + timedelta(minutes=arrival)

def main(): 
    station_arrivals()

if __name__ == '__main__': 
    main()