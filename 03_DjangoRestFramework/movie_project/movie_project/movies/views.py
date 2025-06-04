from django.shortcuts import render
from rest_framework.decorators import api_view # Allows us to define GET, POST, etc.
from rest_framework.response import Response   # For sending JSON responses
from rest_framework import status              # Status codes like 200, 404, 400
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
#movie_list – GET all movies, POST a new movie
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all() # get all the movie record from DB
        serializer = MovieSerializer(movies, many=True) # serialize the list of movies
        return Response(serializer.data) # send serialized data as JSON
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data = request.data) #deserialize the incomming data
        if serializer.is_valid(): # validate the data
            serializer.save() # Calls create() method in serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # If invalid

# movie_detail – GET, PUT, DELETE a single movie by ID
@api_view(['GET', 'PUT', 'DELETE'])               # This view supports GET, PUT, DELETE
def movie_detail(request, pk):                    # pk = primary key (movie ID)
    try:
        movie = Movie.objects.get(pk=pk)          # Try to get the movie by ID
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)       # Serialize the movie
        return Response(serializer.data)          # Return the JSON data

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)  # Deserialize + bind to existing movie
        if serializer.is_valid():                 # Validate input
            serializer.save()                     # Calls update() method in serializer
            return Response(serializer.data)      # Return updated movie data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()                            # Delete the movie from DB
        return Response(status=status.HTTP_204_NO_CONTENT)  # No content response

    
