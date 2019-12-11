from django.db import models
from django.contrib.auth.models import User
from apps.core import bart

class FavoriteStation(models.Model): 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    station_list = [(station['abbr'], station['name']) for station in bart.stations()]

    station = models.CharField(
        max_length=30, 
        choices=station_list,
    )
    class Meta:
        unique_together = ["user", "station",]

    def __str__(self):
        return self.user.username + ': ' + self.station