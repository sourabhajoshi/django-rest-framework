from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BookListCreateView(APIView):
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
