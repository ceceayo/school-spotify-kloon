from django.contrib import admin

from .models import Album, Artist, Music, MusicTrack

# Register your models here.
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(MusicTrack)
admin.site.register(Artist)
