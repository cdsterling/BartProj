from django.db import models

class StationArrival(models.Model):
    """
    Examples on how to use the data: 

        # pull all data 
        arrivals = [row.station_abbr for row in StationArrival.objects.all()]

        # get a list of distinct station name abbreviations
        stations = list(set(station for station in arrivals['station_abbr']))

    Some observations about the API: 
        - arrival_minutes will sometimes return "Leaving," presumably when the arrival_minutes is <= 0
    """
    update_datetime = models.DateTimeField()
    station_name = models.CharField(max_length=100)
    station_abbr = models.CharField(max_length=30)
    destination_name = models.CharField(max_length=100)
    destination_abbr = models.CharField(max_length=30)
    arrival_minutes = models.CharField(max_length=30)
    arrival_datetime = models.DateTimeField()
    platform = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    length = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    hexcolor = models.CharField(max_length=30)
    bikeflag = models.CharField(max_length=30)
    delay_seconds = models.IntegerField()