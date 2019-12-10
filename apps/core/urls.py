from django.urls import path

from apps.core import views

'.site.com/home'

urlpatterns = [
    path('', views.homepage_logged_out, name='homepage'), #homepage_logged_out
    path('home/', views.homepage_logged_in, name='home'),   #homepage_logged_in
    path('about/', views.about, name='about'),
]
