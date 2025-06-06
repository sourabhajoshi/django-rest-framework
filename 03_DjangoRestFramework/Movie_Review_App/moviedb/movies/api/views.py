from .movies.models import Movies
from django.http import JsonResponse

# def movie_list(request):
#     pass
#


# Create your views here.
def movie_list(request):
    movies = Movies.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

def get_movie(request, pk):
    movies = Movies.objects.get(pk=pk)
    data = {
        'title' : movies.title
    }
    return JsonResponse(data)