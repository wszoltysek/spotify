import pytest
from main_app.models import *
from main_app.tests.utils import *


# TESTS FOR CREATE MODELS:

@pytest.mark.django_db
def test_create_user():
    """
    Should create new user object and save it to database
    """
    # Given:
    users_before = User.objects.count()
    # When:
    new_user = create_fake_user()
    # Then:
    assert User.objects.count() == users_before + 1
    assert new_user.pk == 1
    assert new_user.is_anonymous == False


@pytest.mark.django_db
def test_create_genre():
    """
    Should create new genre object and save it to database
    """
    # Given:
    genres_before = Genre.objects.count()
    # When:
    new_genre = create_fake_genre()
    # Then:
    assert Genre.objects.count() == genres_before + 1
    assert Genre.objects.count() == 1
    assert new_genre.pk == 1
    assert new_genre.user.pk == 2


@pytest.mark.django_db
def test_create_artist():
    """
    Should create new artist object and save it to database
    """
    # Given:
    artists_before = Artist.objects.count()
    # When:
    new_artist = create_fake_artist()
    # Then:
    assert Artist.objects.count() == artists_before + 1
    assert Artist.objects.count() == 1
    assert new_artist.pk == 1


@pytest.mark.django_db
def test_create_track():
    """
    Should create new track object and save it to database
    """
    # Given:
    tracks_before = Track.objects.count()
    # When:
    new_track = create_fake_track()
    # Then:
    assert Track.objects.count() == tracks_before + 1
    assert Track.objects.count() == 1
    assert new_track.pk == 1
