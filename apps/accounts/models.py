from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core import bart


# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!

class User(AbstractUser):

    station_list = [(station['abbr'], station['name']) for station in bart.stations()]

    favorite_station1 = models.CharField(
        max_length=30, 
        choices=station_list,
    )

    favorite_station2 = models.CharField(
        max_length=30, 
        choices=station_list,
    )

    favorite_station3 = models.CharField(
        max_length=30, 
        choices=station_list,
    )

