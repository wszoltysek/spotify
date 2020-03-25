from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView

from .models import *
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, "_base_.html")


class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "_dashboard_.html")


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
        else:
            print(form.errors)
            ctx = {"form": form}
            return render(request, "user/register.html", ctx)


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        ctx = {"form": form}
        return render(request, "user/login.html", ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect("/dashboard/")
            else:
                error = "Brak takiego użytkownika lub błędne hasło."
                ctx = {"form": form, "error": error}
                return render(request, "user/login.html", ctx)


class UserLogout(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'user/logout.html')

    def post(self, request):
        logout(request)
        return redirect('/')


class UserPanel(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        genre_count = len(Genre.objects.filter(user=request.user))
        artist_count = len(Artist.objects.filter(user=request.user))
        track_count = len(Track.objects.filter(user=request.user))
        ctx = {
            "genre_count": genre_count,
            "artist_count": artist_count,
            "track_count": track_count
        }
        return render(request, "user/user_panel.html", ctx)


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
            Genre.objects.create(
                user=request.user,
                name=form.cleaned_data['name']
            )
            return redirect('/genrelist/')
        else:
            print(form.errors)
            ctx = {"form": form}
            return render(request, "genre_add.html", ctx)


class GenreList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        genres = Genre.objects.filter(user=request.user).order_by("name")
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
    fields = ['name']
    success_url = '/genrelist/'
    template_name = 'genre_update_form.html'


class GenreDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Genre
    success_url = '/genrelist/'
    template_name = 'confirm_delete.html'


# ARTIST:

class ArtistAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = ArtistAddForm()
        form.fields['genre'].queryset = Genre.objects.filter(user=request.user)
        ctx = {"form": form}
        return render(request, "artist_add.html", ctx)

    def post(self, request):
        form = ArtistAddForm(request.POST)
        if form.is_valid():
            Artist.objects.create(
                user=request.user,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                genre=form.cleaned_data['genre']
            )
            return redirect('/artistlist/')
        else:
            print(form.errors)
            ctx = {"form": form}
            return render(request, "artist_add.html", ctx)


class ArtistList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        artists = Artist.objects.filter(user=request.user).order_by("name")
        ctx = {"artists": artists}
        return render(request, "artist_list.html", ctx)


class ArtistDetails(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        artist = Artist.objects.get(pk=id)
        track = Track.objects.filter(artist_id=artist.id)
        ctx = {"artist": artist, "track": track}
        return render(request, "artist_details.html", ctx)


class ArtistUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Artist
    fields = ['name', 'description', 'genre']
    success_url = '/artistlist/'
    template_name = 'artist_update_form.html'


class ArtistDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Artist
    success_url = '/artistlist/'
    template_name = 'confirm_delete.html'


# TRACK:

class TrackAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = TrackAddForm()
        form.fields['artist'].queryset = Artist.objects.filter(user=request.user)
        ctx = {"form": form}
        return render(request, "track_add.html", ctx)

    def post(self, request):
        form = TrackAddForm(request.POST)
        if form.is_valid():
            Track.objects.create(
                user=request.user,
                artist=form.cleaned_data['artist'],
                title=form.cleaned_data['title'],
                label=form.cleaned_data['label'],
                length=form.cleaned_data['length'],
                bpm=form.cleaned_data['bpm'],
                release_date=form.cleaned_data['release_date'],
                link_yt=form.cleaned_data['link_yt']
            )
            return redirect('/tracklist/')
        else:
            print(form.errors)
            ctx = {"form": form}
            return render(request, "track_add.html", ctx)


class TrackList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        tracks = Track.objects.filter(user=request.user).order_by("artist")
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
    fields = ['artist', 'title', 'label', 'length', 'bpm', 'release_date', 'link_yt']
    success_url = '/tracklist/'
    template_name = 'track_update_form.html'


class TrackDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Track
    success_url = '/tracklist/'
    template_name = 'confirm_delete.html'
