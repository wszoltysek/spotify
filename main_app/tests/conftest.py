import os
import sys
import pytest
from main_app.tests.utils import *

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def set_up_genre():
    data = [create_fake_genre() for i in range(5)]
    return data


@pytest.fixture
def set_up_artist():
    data = [create_fake_artist() for i in range(5)]
    return data


@pytest.fixture
def set_up_track():
    data = [create_fake_track() for i in range(5)]
    return data
