from django.urls import path

from .views import (
    HomePageView,
    LikeOrDislikeView,
    MyPlaylistsView,
    PlaylistDetailView,
    SinglePageView,
)

urlpatterns = [
    path("pages/main", HomePageView.as_view(), name="home"),
    path("pages/my-playlists", MyPlaylistsView.as_view()),
    path("pages/pl/<int:pk>", PlaylistDetailView.as_view()),
    path("", SinglePageView.as_view(), name="main"),
    path("api/set_opinion", LikeOrDislikeView, name="set_opinion"),
]
