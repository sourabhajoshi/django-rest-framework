from django.urls import path, include
from .views import mov

urlpatterns = [
    path('', movie_list, name="movie-list"),
]