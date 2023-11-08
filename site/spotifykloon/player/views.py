from dataclasses import dataclass
from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, TemplateView

from .models import Artist, Music, MusicTrack, OpinionOnSong, Playlist, PlaylistItem


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
        context["filler"] = range(3 - (len(music) % 3))
        return context


class SinglePageView(LoginRequiredMixin, TemplateView):
    template_name = "main.html"


@login_required
@require_http_methods(["POST"])
def LikeOrDislikeView(request):
    assert "opinion" in request.POST.keys()
    assert "music" in request.POST.keys()
    assert "artist" in request.POST.keys()

    print(request.user)
    print(request.POST["opinion"])
    opinions = OpinionOnSong.objects.filter(
        user=request.user, song=request.POST["music"], artist=request.POST["artist"]
    )
    print(len(opinions.all()))
    match (len(opinions.all())):
        case 0:
            OpinionOnSong(
                user=request.user,
                artist=Artist.objects.get(pk=int(request.POST["artist"])),
                song=Music.objects.get(pk=int(request.POST["music"])),
                opinion="1" if (request.POST["opinion"] == "true") else "-1",
            ).save()
            return HttpResponse("added")
        case 1:
            x = opinions.first()
            x.opinion = (
                "1"
                if (
                    request.POST["opinion"] == "true"
                    and opinions.first().opinion in {"0", "-1"}
                )
                else "0"
                if (
                    request.POST["opinion"] == "true"
                    and opinions.first().opinion == "1"
                )
                else "-1"
                if (
                    request.POST["opinion"] == "false"
                    and opinions.first().opinion in {"0", "1"}
                )
                else "0"
            )
            x.save()
            return HttpResponse("changed")
        case _:
            assert False


class MyPlaylistsView(ListView):
    model = Playlist
    template_name = "playlist-list.html"

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "playlist-info.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["songs"] = PlaylistItem.objects.filter(pl=ctx["object"]).all()
        return ctx
