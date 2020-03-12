import os
import sys
import pytest

from main_app.tests.utils import create_fake_genre

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def set_up_genre():
    data = []
    for _ in range(5):
        genre = create_fake_genre()
        data.append(genre)
    return data
