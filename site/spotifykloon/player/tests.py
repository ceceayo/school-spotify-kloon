from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files import File
from django.test import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .models import Album, Artist, Music, MusicTrack

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


class HomePageTest(StaticLiveServerTestCase):
    fixtures = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        get_user_model().objects.create_user("myuser", "", "secret")

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/accounts/login")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("myuser")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("secret")
        self.selenium.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        self.assertEqual(self.selenium.current_url, f"{self.live_server_url}/")
