from django.urls import path

from .views import HomePageView, SinglePageView

urlpatterns = [
    path("pages/main", HomePageView.as_view(), name="home"),
    path("", SinglePageView.as_view(), name="main"),
]
