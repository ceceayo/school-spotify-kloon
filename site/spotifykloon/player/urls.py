from django.urls import path

from .views import HomePageView, LikeOrDislikeView, SinglePageView, MyPlaylistsView, PlaylistDetailView

urlpatterns = [
    path("pages/main", HomePageView.as_view(), name="home"),
    path("pages/pl", MyPlaylistsView.as_view(), name="playlists"),
    path("pages/pl/<int:pk>", PlaylistDetailView.as_view(), name="playlist_info"),
    path("", SinglePageView.as_view(), name="main"),
    path("api/set_opinion", LikeOrDislikeView, name="set_opinion"),
]
