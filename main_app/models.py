from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    length = models.FloatField()
    bpm = models.IntegerField()
    release_date = models.DateField()
    link_yt = models.CharField(max_length=200)
