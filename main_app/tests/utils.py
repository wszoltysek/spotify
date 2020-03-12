from faker import Faker
from main_app.models import *
from random import randint, choice

faker = Faker("pl_PL")


def create_fake_genre():
    """Generate new genre and saves to database"""
    new_genre = Genre.objects.create(
        name=faker.word()
    )
    return new_genre
