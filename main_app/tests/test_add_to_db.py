import pytest
from main_app.models import *
from main_app.tests.utils import create_fake_genre


@pytest.mark.django_db
def test_add_genre(set_up_genre):
    """
    Should create new genre object and save it to database
    """
    # Given:
    genre_before = Genre.objects.count()
    # When:
    new_genre = create_fake_genre()
    # Then:
    assert Genre.objects.count() == genre_before + 1
    assert Genre.objects.count() == 6
