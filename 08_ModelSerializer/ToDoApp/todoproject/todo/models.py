from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    due_date = models.DateField()
    
    def __str__(self):
        return self.title
