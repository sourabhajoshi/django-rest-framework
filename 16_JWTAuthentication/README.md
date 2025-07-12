# JWT Authentication 

In Django REST Framework (DRF), JWT is commonly used to authenticate APIs in a stateless way — no session or cookie is stored on the server.

### **JWT Authentication Flow (Concept)**
- User logs in with username/password.
- If valid, the server returns a JWT token (access + optional refresh).
- The client (e.g., frontend or mobile app) stores the token (usually in localStorage).
- On every request, the client sends the token in the Authorization header.
- The server verifies the token and identifies the user.

### **Step-by-Step: Implement JWT Auth in DRF**

We'll use djangorestframework-simplejwt, a standard library for JWT in DRF.

Step1 : Create and install required packages:
```
pip install django djangorestframework djangorestframework-simplejwt
django-admin startproject jwt_project
cd jwt_project
python manage.py startapp tasks
```

Step2 : Update settings.py
```
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework_simplejwt',
    'tasks',
]

# Configure DRF to use JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

```

Step3 : models.Model (Define Task model)
```
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

//Migrate the fields
python manage.py makemigrations
python manage.py migrate

```

Step4 : ModelSerializer
```
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']  # prevent user from manually setting this
```

Step5 : ModelViewSet + JWT Auth
```
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return tasks for the authenticated user
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Set the owner as the current user
        serializer.save(owner=self.request.user)

```

Step 6 : URLs
```
<!-- tasks/urls.py -->
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

<!-- jwt_project/urls.py -->
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

```

Step 7 : Testing in Postman (Step-by-Step)

1. Create Superuser
```
python manage.py createsuperuser
```

2. Get JWT Tokens
```
POST /api/token/
{
  "username": "admin",
  "password": "yourpassword"
}

Response:
{
  "access": "....",
  "refresh": "...."
}
```

3. Use Access Token
For all task API calls, set this header:
```
Authorization: Bearer <access_token>
```

4. Example: Create a Task
```
POST /api/tasks/

{
  "title": "Complete DRF JWT Project",
  "description": "Finish and test the project before lunch",
  "is_completed": false
}
```
Only the authenticated user can see/edit/delete their tasks.

