from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from apps.accounts.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'favorite_station1',
            'favorite_station2',
            'favorite_station3',
        )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'favorite_station1',
            'favorite_station2',
            'favorite_station3',
        )

