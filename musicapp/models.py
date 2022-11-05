from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Artiste (models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length=500)
    date_released = models.DateTimeField(default = timezone.now)
    likes = models.ManyToManyField(User, blank = True)
    artiste = models.ForeignKey(
        Artiste, on_delete=models.CASCADE, related_name='songs')

    def __str__(self) -> str:
        return self.title

class Lyric (models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.song.title} Lyrics"


    