from django.shortcuts import render
from .models import Movies
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    movies = Movies.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)
