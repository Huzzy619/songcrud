from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)

class Song(models.Model):
    title = models.CharField(max_length = 500)
    date_released = models.DateTimeField(auto_now_add = True)
    likes = models.ManyToManyField(User)
    artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE, related_name = 'songs')

class Lyric (models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete = models.CASCADE)



