from dataclasses import dataclass

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Artist, Music, MusicTrack, OpinionOnSong
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@dataclass
class MusicItem:
    music: Music
    tracks: list[MusicTrack]
    artist: Artist


class HomePageView(LoginRequiredMixin, TemplateView):
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


class SinglePageView(LoginRequiredMixin, TemplateView):
    template_name = "main.html"


@login_required
@require_http_methods(["POST"])
def LikeOrDislikeView(request):
    assert 'opinion' in request.POST.keys()
    assert 'music' in request.POST.keys()
    assert 'artist' in request.POST.keys()

    print(request.user)
    print(request.POST['opinion'])
    opinions = OpinionOnSong.objects.filter(
        user=request.user, song=request.POST["music"], artist=request.POST["artist"])
    print(len(opinions.all()))
    assert request.POST['opinion'] in {"-1", "0", "1"}
    match(len(opinions.all())):
        case 0:
            return HttpResponse("added")
        case 1:
            opinions.all().update(opinion=request.POST['opinion'])
            return HttpResponse("changed")
        case _:
            assert False
