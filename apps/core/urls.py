from django.urls import path

from apps.core import views

'.site.com/home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('show_single_station/<stn_abbr>/', views.show_single_station, name="show_station"),
]
