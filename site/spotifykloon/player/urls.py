from django.urls import path  
from .views import HomePageView, SinglePageView, NoAuthenticationView

urlpatterns = [  
    path('pages/main', HomePageView.as_view(), name='home'),  
    path('', SinglePageView.as_view(), name="main"),
    path('', NoAuthenticationView.as_view(), name="login"),
]