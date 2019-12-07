from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('preferences/', views.preferences, name='preferences'),
]
