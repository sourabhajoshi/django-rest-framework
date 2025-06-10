# Custom Serializer in DRF

### **What is Serializer?**

A serializer is like a translator. It converts your model (Python object) into JSON (for API) and vice versa.

```
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    published = serializers.DateField()
```

### **What is ModelSerializer?**

A ModelSerializer automatically: Reads your Django model, Converts fields into JSON and Validates and saves data.
```
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```
This works for basic CRUD (Create, Read, Update, Delete).

### **What is a Custom Serializer?**

It means you add extra logic or fields into your serializer, because the default serializer is not enough for your case.

For example
```
<!-- model.py -->
# Task model
class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()

<!-- Serializers.py -->
from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    # Extra field (not in model): days_remaining
    # This will calculate how many days are left until due_date
    days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = Task  # Link this serializer to Task model
        fields = ['id', 'title', 'description', 'due_date', 'is_complete', 'days_remaining']
        # Include both model fields and our custom field

    # This method supports SerializerMethodField
    def get_days_remaining(self, obj):
        # obj is the Task object
        if obj.due_date:
            return (obj.due_date - date.today()).days
        return None

    # Custom validation for a specific field (title)
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    # Custom validation for multiple fields (optional)
    def validate(self, data):
        if data.get('is_complete') and not data.get('due_date'):
            raise serializers.ValidationError("Completed tasks must have a due date.")
        return data

    # Custom logic while creating an object
    def create(self, validated_data):
        print("Creating a new task:", validated_data)
        return super().create(validated_data)

    # Custom logic while updating an object (optional)
    def update(self, instance, validated_data):
        print(f"Updating Task [{instance.title}] with:", validated_data)
        return super().update(instance, validated_data)

```

**Scenario: OTT Streaming Platform**

- You’re building an API for a streaming service like Netflix or Amazon Prime.
- A StreamPlatform is a streaming provider like Netflix, Hotstar, etc.
- Each platform has multiple WatchList items (movies/TV shows).


Create a folder, install django and djangorestframework, create a project (StreamPlatform) and app (watch)

Create a table and fields from app/models.py
```
from django.db import models

# StreamPlatform model represents a streaming provider (like Netflix, Prime)
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)  # Name of the platform
    about = models.TextField()               # Short description
    website = models.URLField()              # Website link

    def __str__(self):
        return self.name


# WatchList model represents a movie or TV show
class WatchList(models.Model):
    title = models.CharField(max_length=100)        # Title of the content
    storyline = models.TextField()                  # Short storyline/description
    active = models.BooleanField(default=True)      # Whether the content is currently active
    created = models.DateTimeField(auto_now_add=True)  # Auto timestamp when added

    # ForeignKey to StreamPlatform (one-to-many relationship)
    platform = models.ForeignKey(
        StreamPlatform,
        related_name="watchlist",  # Enables reverse access like: stream.watchlist.all()
        on_delete=models.CASCADE   # If platform is deleted, its content is also deleted
    )

    def __str__(self):
        return self.title

```

run the command to save table and fields into db
```
python manage.py makemigrations
python manage.py migrate
```

Create Serializers
```
from rest_framework import serializers
from .models import StreamPlatform, WatchList

# Serializer for WatchList model
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'  # You can also list fields manually like ['id', 'title', 'platform']

# Serializer for StreamPlatform model
class StreamPlatformSerializer(serializers.ModelSerializer):
    # Show related watchlist items as nested objects
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
```

Create ViewSets
```
from rest_framework import viewsets
from .models import StreamPlatform, WatchList
from .serializers import StreamPlatformSerializer, WatchListSerializer

# ViewSet for StreamPlatform (CRUD)
class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# ViewSet for WatchList (CRUD)
class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
```

Register Routes with Router
```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamPlatformViewSet, WatchListViewSet

# Automatically generates all URL patterns for ViewSets
router = DefaultRouter()
router.register(r'stream', StreamPlatformViewSet, basename='streamplatform')
router.register(r'watch', WatchListViewSet, basename='watchlist')

urlpatterns = [
    path('', include(router.urls)),
]
```

Add App to Project URLs
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app_name.urls')),  # replace with your app name
]
```

Run the application and perform the CRUD opertaion
