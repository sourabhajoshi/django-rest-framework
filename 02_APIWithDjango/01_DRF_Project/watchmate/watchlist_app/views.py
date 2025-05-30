from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse


# Create your views here. : Function based view
# Return all the elements
def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    print(movies.values())

    return JsonResponse(
        data)  # {"movies": [{"id": 1, "name": "Movie1", "description": "Description-1", "active": true},
    # {"id": 2, "name": "movie2", "description": "Description-2", "active": false}]}


# Return individual element based on pk (primary key) value
def movie_detals(request, pk):
    movies = Movie.objects.get(pk=pk)
    data = {
        'name': movies.name,
        'description': movies.description,
        'active': movies.active
    }

    return JsonResponse(data) #{"name": "Movie1", "description": "Description-1", "active": true}
