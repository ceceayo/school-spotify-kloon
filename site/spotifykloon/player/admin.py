from django.contrib import admin

from .models import Artist, Music, MusicTrack, OpinionOnSong

# Register your models here.
admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(MusicTrack)
admin.site.register(OpinionOnSong)
