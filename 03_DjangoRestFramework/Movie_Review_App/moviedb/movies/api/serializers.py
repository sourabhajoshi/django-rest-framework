from rest_framework.serializers import Serializer

class MovieSerialize(Serializer.Serializer):
    id = Serializer.IntegerField(read_only=True)
    title = Serializer.CharField()
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
