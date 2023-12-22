from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ManyToManyField(Album)
    duration = models.PositiveIntegerField()
    track_number = models.PositiveIntegerField(unique=True)
    lyrics = models.TextField()

    def __str__(self):
        return self.title
