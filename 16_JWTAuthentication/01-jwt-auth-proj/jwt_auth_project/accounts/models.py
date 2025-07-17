from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser is a Django-provided abstract base class that contains all the fields and functionality of the default User model (like username, email, password, first_name, last_name, etc.).

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username