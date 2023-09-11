from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.TextField()


class MusicTrack(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to='static/music/')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

