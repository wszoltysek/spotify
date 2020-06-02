from faker import Faker
from main_app.models import *
from random import randint

faker = Faker("pl_PL")


def create_fake_user():
    """
    Generate new user and saves to database
    """
    user = User.objects.create(username=faker.first_name_male())
    return user


def create_fake_genre():
    """
    Generate new genre and saves to database
    """
    new_genre = Genre.objects.create(
        user=create_fake_user(),
        name=faker.word()
    )
    return new_genre


def create_fake_artist():
    """
    Generate new artist and saves to database
    """
    new_artist = Artist.objects.create(
        name=faker.word(),
        description=faker.sentence(),
        genre=create_fake_genre()
    )
    return new_artist


def create_fake_track():
    """
    Generate new track and saves to database
    """
    new_track = Track.objects.create(
        artist=create_fake_artist(),
        title=faker.name(),
        label=faker.word(),
        length=randint(1, 5),
        bpm=randint(1, 124),
        release_date=faker.date(),
        link_yt=faker.word()
    )
    return new_track
