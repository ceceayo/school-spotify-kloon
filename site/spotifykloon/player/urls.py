from django.urls import path

from .views import HomePageView, SinglePageView, LikeOrDislikeView

urlpatterns = [
    path("pages/main", HomePageView.as_view(), name="home"),
    path("", SinglePageView.as_view(), name="main"),
    path("api/set_opinion", LikeOrDislikeView, name="set_opinion")
]
