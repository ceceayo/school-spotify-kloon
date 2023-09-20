from django.views.generic import TemplateView
from .models import Music, MusicTrack, Artist
from dataclasses import dataclass


@dataclass
class MusicItem:
    musicItem: Music
    tracks: list[MusicTrack]
    artist: Artist


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = Music.objects.all()
        result = []
        for item in music:
            tracks = MusicTrack.objects.filter(music=item)
            artist = Artist.objects.filter(id=item.artist_id).first()
            result.append(MusicItem(item, tracks, artist))
        context["music"] = result
        return context
