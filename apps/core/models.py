from django.db import models

# query this table for specific stations, destination
class StationArrival(models.Model):
    update_datetime = models.DateTimeField()
    station_name = models.CharField(max_length=100)
    station_abbreviation = models.CharField(max_length=30)
    destination_name = models.CharField(max_length=100)
    destination_abbreviation = models.CharField(max_length=30)
    arrival_minutes = models.IntegerField()
    arrival_datetime = models.DateTimeField()
    platform = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    length = models.IntegerField()
    color = models.CharField(max_length=30)
    hexcolor = models.CharField(max_length=30)
    bikeflag = models.IntegerField()
    seconds_delayed = models.IntegerField()