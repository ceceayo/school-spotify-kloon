from dataclasses import dataclass

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Music, MusicTrack


@dataclass
class MusicItem:
    musicItem: Music
    tracks: list[MusicTrack]


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = Music.objects.all()
        result = []
        for item in music:
            tracks = MusicTrack.objects.filter(music=item)
            result.append(MusicItem(item, tracks))
        context["music"] = result
        return context


class SinglePageView(LoginRequiredMixin, TemplateView):
    template_name = "main.html"
