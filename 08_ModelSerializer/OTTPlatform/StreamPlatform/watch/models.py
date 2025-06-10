from django.db import models

# StreamPlatform model represents a streaming provider (like Netflix, Prime)
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField()
    
    def __str__(self):
        return self.name

# WatchList model represents a movie or TV show
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # one to many relationship : Foreignkey to Streamplatform
    platform = models.ForeignKey(
        StreamPlatform,
        related_name="watchList", # Enables reverse access like: stream.watchlist.all()
        on_delete=models.CASCADE  # If platform is deleted, its content is also deleted
    )
    
    def __str__(self):
        return self.title
    