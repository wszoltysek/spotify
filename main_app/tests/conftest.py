import os
import sys
import pytest

from main_app.tests.utils import create_fake_genre, create_fake_artist

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def set_up_genre():
    data = []
    for _ in range(5):
        genre = create_fake_genre()
        data.append(genre)
    return data


@pytest.fixture
def set_up_artist():
    data = []
    for _ in range(5):
        artist = create_fake_artist()
        data.append(artist)
    return data

