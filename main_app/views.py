from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView

from .models import *
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, "_base_.html")


class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        genre_count = Genre.objects.count()
        artist_count = Artist.objects.count()
        track_count = Track.objects.count()
        ctx = {"genre_count": genre_count, "artist_count": artist_count, "track_count": track_count}
        return render(request, "_dashboard_.html", ctx)


# USER:

class UserRegister(View):
    def get(self, request):
        form = UserRegisterForm()
        ctx = {"form": form}
        return render(request, "user/register.html", ctx)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')

        ctx = {"form": form}
        return render(request, "user/register.html", ctx)


class UserPanel(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "user/user_panel.html")


# GENRE:

class GenreAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = GenreAddForm()
        ctx = {"form": form}
        return render(request, "genre_add.html", ctx)

    def post(self, request):
        form = GenreAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/genrelist/')

        ctx = {"form": form}
        return render(request, "genre_add.html", ctx)


class GenreList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        genres = Genre.objects.all()
        ctx = {"genres": genres}
        return render(request, "genre_list.html", ctx)


class GenreDetails(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        genre = Genre.objects.get(pk=id)
        artist = Artist.objects.filter(genre_id=genre.id)
        ctx = {"genre": genre, "artist": artist}
        return render(request, "genre_details.html", ctx)


class GenreUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Genre
    fields = '__all__'
    success_url = '/genrelist/'
    template_name = 'genre_update_form.html'


# TODO search

# ARTIST:

class ArtistAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = ArtistAddForm()
        ctx = {"form": form}
        return render(request, "artist_add.html", ctx)

    def post(self, request):
        form = ArtistAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artistlist/')

        ctx = {"form": form}
        return render(request, "artist_add.html", ctx)


class ArtistList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        artists = Artist.objects.all()
        ctx = {"artists": artists}
        return render(request, "artist_list.html", ctx)


class ArtistDetails(View):
    def get(self, request, id):
        artist = Artist.objects.get(pk=id)
        track = Track.objects.filter(artist_id=artist.id)
        ctx = {"artist": artist, "track": track}
        return render(request, "artist_details.html", ctx)


class ArtistUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Artist
    fields = '__all__'
    success_url = '/artistlist/'
    template_name = 'artist_update_form.html'


def delete_artist(request, id):
    artist = Artist.objects.get(pk=id)
    artist.delete()
    return redirect('/artistlist/')


# TODO search

# TRACK:

class TrackAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = TrackAddForm()
        ctx = {"form": form}
        return render(request, "track_add.html", ctx)

    def post(self, request):
        form = TrackAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tracklist/')

        ctx = {"form": form}
        return render(request, "track_add.html", ctx)


class TrackList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        tracks = Track.objects.all().order_by("artist__genre")
        ctx = {"tracks": tracks}
        return render(request, "track_list.html", ctx)


class TrackDetails(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        track = Track.objects.get(pk=id)
        ctx = {"track": track}
        return render(request, "track_details.html", ctx)


class TrackUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Track
    fields = '__all__'
    success_url = '/tracklist/'
    template_name = 'track_update_form.html'


def delete_track(request, id):
    track = Track.objects.get(pk=id)
    track.delete()
    return redirect('/tracklist/')

# TODO search
