from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.artist.name} - {self.title}"


class MusicTrack(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='static/music/')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} for {self.music.title} by {self.music.artist.name}"
