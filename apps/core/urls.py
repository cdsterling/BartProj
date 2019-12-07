from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('show_station/<stn_abbr>/', views.show_station, name="show_station")
]
