from django.urls import path

from apps.core import views

'.site.com/home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home_logged_in/', views.home_logged_in, name='home_logged_in')]
