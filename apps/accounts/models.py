from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core import bart


class User(AbstractUser):
    pass

class FavoriteStation(): 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    station_list = [(station['abbr'], station['name']) for station in bart.stations()]

    station = models.CharField(
        max_length=30, 
        choices=station_list,
        blank=True,
    )