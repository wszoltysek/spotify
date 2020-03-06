from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64)


class Artist(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = #TODO - DODANIE DO ALBUMU OPCJONALNIE ??
    title = models.CharField(max_length=64)
    label = models.CharField(max_length=100)
    length = models.FloatField()
    bpm = models.IntegerField()
    release_date = models.DateField()
    link_yt = models.TextField()


class Album (models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

