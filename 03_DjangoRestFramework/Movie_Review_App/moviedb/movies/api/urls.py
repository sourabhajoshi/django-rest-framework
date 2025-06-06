from django.urls import path, include
from .views import movie_list, get_movie

urlpatterns = [
    path('', movie_list, name="movie-list"),
    path('<int:pk>', get_movie, name="get-movie")
]