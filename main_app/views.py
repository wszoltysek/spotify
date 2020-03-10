from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, "_base_.html")


class DashboardView(View):
    def get(self, request):
        return render(request, "_dashboard_.html")


# GENRE:

class GenreAdd(View):
    def get(self, request):
        form = GenreAddForm()
        ctx = {"form": form}
        return render(request, "genre_add.html", ctx)

    def post(self, request):
        form = GenreAddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/genrelist/')


class GenreList(View):
    def get(self, request):
        genres = Genre.objects.all()
        ctx = {"genres": genres}
        return render(request, "genre_list.html", ctx)


class GenreDetails(View):
    def get(self, request, id):
        genre = Genre.objects.get(pk=id)
        artist = Artist.objects.filter(genre_id=genre.id)
        ctx = {"genre": genre, "artist": artist}
        return render(request, "genre_details.html", ctx)


# TODO search, modify, delete

# ARTIST:

class ArtistAdd(View):
    def get(self, request):
        form = ArtistAddForm()
        ctx = {"form": form}
        return render(request, "artist_add.html", ctx)

    def post(self, request):
        form = ArtistAddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/artistlist/')


class ArtistList(View):
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


# TODO search, modify, delete

# TRACK:

class TrackAdd(View):
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


class TrackList(View):
    def get(self, request):
        tracks = Track.objects.all().order_by("artist__genre")
        ctx = {"tracks": tracks}
        return render(request, "track_list.html", ctx)


class TrackDetails(View):
    def get(self, request, id):
        track = Track.objects.get(pk=id)
        ctx = {"track": track}
        return render(request, "track_details.html", ctx)


def delete_track (request, id):
    try:
        track = Track.objects.get(pk=id)
    except:
        return redirect('/tracklist/')

    track.delete()
    return redirect('/tracklist/')

# TODO search, modify
