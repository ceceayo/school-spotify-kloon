from django.core.files import File
from django.test import TestCase

from .models import Artist, Album, Music, MusicTrack


# Create your tests here.


class ModelsTest(TestCase):
    def test_models(self):
        artist = Artist.objects.create(name="test")
        self.assertEqual(artist.name, "test")
        artist.save()
        self.assertEqual(artist in Artist.objects.all(), True)
        album = Album.objects.create(title="aaaa", artist=artist)
        self.assertEqual(album.title, "aaaa")
        self.assertEqual(album.artist, artist)
        album.save()
        self.assertEqual(album in Album.objects.all(), True)
        music = Music.objects.create(title="bbbb", album=album)
        self.assertEqual(music.title, "bbbb")
        self.assertEqual(music.album, album)
        self.assertEqual(music.album.artist, artist)
        music.save()
        self.assertEqual(music in Music.objects.all(), True)
        self.assertEqual(music.album.artist.name, "test")

    def test_musictrack(self):
        artist = Artist.objects.create(name="test")
        artist.save()
        album = Album.objects.create(title="aaaa", artist=artist)
        album.save()
        music = Music.objects.create(title="bbbb", album=album)
        music.save()
        musictrack = MusicTrack.objects.create(
            title="cccc",
            music=music,
            file=File(open("testing/Mann_gegen_Mann.mp3", "rb")),
        )

    def tearDown(self):
        import os

        os.system("rm static/music/testing/*")
