from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from main_app.models import *


class GenreAddForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class ArtistAddForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description', 'genre']


class TrackAddForm(ModelForm):
    class Meta:
        model = Track
        fields = ['artist', 'title', 'label', 'length', 'bpm', 'release_date', 'link_yt']
        widgets = {
            'length': TextInput(attrs={'placeholder': '4.22'}),
            'release_date': TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'link_yt': TextInput(attrs={'placeholder': 'ex. ViwtNLUqkMY'}),
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    login = forms.CharField(label="Login", max_length=32)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
