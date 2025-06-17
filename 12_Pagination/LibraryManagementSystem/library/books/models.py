from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.title
