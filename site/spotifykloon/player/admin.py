from django.contrib import admin
from .models import Music, MusicTrack, Artist

# Register your models here.
admin.site.register(Music)
admin.site.register(MusicTrack)
admin.site.register(Artist)