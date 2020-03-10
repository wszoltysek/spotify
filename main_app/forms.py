from django import forms
from django.forms import ModelForm

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

