from django import forms
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

