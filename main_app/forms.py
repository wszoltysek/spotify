from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput

from main_app.models import *


class GenreAddForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class ArtistAddForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class TrackAddForm(ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        widgets = {
            'release_date': TextInput(attrs={'placeholder': 'ex. 2020-02-02'}),
            'link_yt': TextInput(attrs={'placeholder': 'ex. ViwtNLUqkMY'}),
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
