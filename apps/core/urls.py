from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('show_single_station/<stn_abbr>/', views.show_single_station, name="show_station"),
    path('show_all_users_stations/', views.show_all_users_stations, name="show_all_stations"),
]
