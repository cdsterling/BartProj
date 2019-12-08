from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from apps.accounts.models import FavoriteStation

class FavoriteStationForm(forms.ModelForm):
    class Meta:
        model = FavoriteStation
        fields = (
            'station',
        )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

