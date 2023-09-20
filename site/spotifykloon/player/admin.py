from django.contrib import admin

from .models import Artist, Music, MusicTrack

# Register your models here.
admin.site.register(Music)
admin.site.register(MusicTrack)
admin.site.register(Artist)
