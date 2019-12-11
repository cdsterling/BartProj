from django.urls import path

from apps.accounts import views

# accounts/...
urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/remove/<station_abbr>', views.remove_favorite, name='remove_favorite'),
]
