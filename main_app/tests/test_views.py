import pytest
from django.test import Client
from main_app.tests.utils import *

client = Client()


# HOMEPAGE / DASHBOARD VIEWS:

def test_view_homepage_get():
    response = client.get("/")
    assert response.status_code == 200


def test_view_dashboard_get():
    response = client.get("/dashboard/")
    assert response.status_code == 302


def test_view_dashboard_post():
    response = client.post("/dashboard/")
    assert response.status_code == 302


# USER VIEWS:

def test_view_login_get():
    response = client.get("/login/")
    assert response.status_code == 200


def test_view_login_post():
    response = client.post("/login/")
    assert response.status_code == 200


def test_view_register_get():
    response = client.get("/register/")
    assert response.status_code == 200


def test_view_register_post():
    response = client.post("/register/")
    assert response.status_code == 200


def test_view_logout_get():
    response = client.get("/logout/")
    assert response.status_code == 302


def test_view_logout_post():
    response = client.post("/logout/")
    assert response.status_code == 302


def test_view_password_change_get():
    response = client.get("/password_change/")
    assert response.status_code == 302


def test_view_password_change_post():
    response = client.post("/password_change/")
    assert response.status_code == 302


def test_view_password_change_done_get():
    response = client.get("/password_change/done/")
    assert response.status_code == 302


def test_view_password_change_done_post():
    response = client.post("/password_change/done/")
    assert response.status_code == 302


def test_view_password_reset_get():
    response = client.get("/password_reset/")
    assert response.status_code == 200


def test_view_user_panel_get():
    response = client.get("/userpanel/")
    assert response.status_code == 302


def test_view_user_panel_post():
    response = client.post("/userpanel/")
    assert response.status_code == 302


# GENRE VIEWS:

def test_view_genre_add_get():
    response = client.get("/addgenre/")
    assert response.status_code == 302


def test_view_genre_add_post():
    response = client.post("/addgenre/")
    assert response.status_code == 302


def test_view_genre_list_get():
    response = client.get("/genrelist/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_genre_details_get():
    genre = create_fake_genre()
    response = client.get(f"/genre/{genre.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_genre_edit_get():
    genre = create_fake_genre()
    response = client.get(f"/genre/update/{genre.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_genre_edit_post():
    genre = create_fake_genre()
    response = client.post(f"/genre/update/{genre.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_genre_delete_get():
    genre = create_fake_genre()
    response = client.get(f"/genre/delete/{genre.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_genre_delete_post():
    genre = create_fake_genre()
    response = client.post(f"/genre/delete/{genre.pk}/")
    assert response.status_code == 302


# ARTIST VIEWS:

def test_view_artist_add_get():
    response = client.get("/addartist/")
    assert response.status_code == 302


def test_view_artist_add_post():
    response = client.post("/addartist/")
    assert response.status_code == 302


def test_view_artist_list_get():
    response = client.get("/artistlist/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_artist_details_get():
    artist = create_fake_artist()
    response = client.get(f"/artist/{artist.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_artist_edit_get():
    artist = create_fake_artist()
    response = client.get(f"/artist/update/{artist.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_artist_edit_post():
    artist = create_fake_artist()
    response = client.post(f"/artist/update/{artist.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_artist_delete_get():
    artist = create_fake_artist()
    response = client.get(f"/artist/delete/{artist.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_artist_delete_post():
    artist = create_fake_artist()
    response = client.post(f"/artist/delete/{artist.pk}/")
    assert response.status_code == 302


# TRACK VIEWS:

def test_view_track_add_get():
    response = client.get("/addtrack/")
    assert response.status_code == 302


def test_view_track_add_post():
    response = client.post("/addtrack/")
    assert response.status_code == 302


def test_view_track_list_get():
    response = client.get("/tracklist/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_track_details_get():
    track = create_fake_track()
    response = client.get(f"/track/{track.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_track_edit_get():
    track = create_fake_track()
    response = client.get(f"/track/update/{track.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_track_edit_post():
    track = create_fake_track()
    response = client.post(f"/track/update/{track.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_track_delete_get():
    track = create_fake_track()
    response = client.get(f"/track/delete/{track.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_track_delete_post():
    track = create_fake_track()
    response = client.post(f"/track/delete/{track.pk}/")
    assert response.status_code == 302
