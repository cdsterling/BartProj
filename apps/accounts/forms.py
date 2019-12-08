from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from apps.accounts.models import User, FavoriteStations

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = User
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

