from django.contrib import admin

from .models import Music, MusicTrack, Artist, Album

# Register your models here.
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(MusicTrack)
admin.site.register(Artist)