from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    duration_minutes = models.IntegerField()
    rating = models.FloatField()
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('THRILLER', 'Thriller'),
        ('ROMANCE', 'Romance'),
    ]

    def __str__(self):
        return self.title
