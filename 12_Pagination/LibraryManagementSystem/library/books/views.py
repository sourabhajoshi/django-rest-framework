from rest_framework import viewsets, filters
from .models import Book
from .serializers import BooksSerializer
from .pagination import BookPagination
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BooksSerializer
    pagination_class = BookPagination
    
    # Add filtering, searching, ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields to filter on
    filterset_fields = ['genre', 'author']

    # Fields to search in
    search_fields = ['title', 'author', 'isbn']

    # Fields to allow ordering
    ordering_fields = ['publication_date', 'title']