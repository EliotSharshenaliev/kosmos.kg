from django.urls import path
from .views import home, home2, home3

urlpatterns = [
    path('home.html', home),
    path('home-02.html', home2),
    path('home-03.html', home3),
]
