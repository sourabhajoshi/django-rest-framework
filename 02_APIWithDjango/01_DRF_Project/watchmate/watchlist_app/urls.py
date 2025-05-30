from django.urls import path, include
from .views import movie_list, movie_detals

urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('<int:pk>', movie_detals, name="movie_detals")
]