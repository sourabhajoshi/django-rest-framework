from django.urls import path, include
from .views import BookListCreateView

urlpatterns = [
    path('book/', BookListCreateView.as_view())
]