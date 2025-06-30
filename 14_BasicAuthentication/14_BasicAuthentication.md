# Authentication 

Authentication is the process of verifying the identity of a user or system. It ensures that the entity trying to access a system is who they claim to be.

Authentication means proving who you are.

Think of it as a security gate that checks who you are before allowing access.

Real-Time Example: ATM Machine
| Step | Action                      | Type           | Description                                                                 |
| ---- | --------------------------- | -------------- | --------------------------------------------------------------------------- |
| 1    | You insert your debit card  | Identification | The ATM recognizes **who you are claiming to be**                           |
| 2    | You enter your 4-digit PIN  | Authentication | The ATM checks if the PIN matches your card’s data                          |
| 3    | PIN is correct              | Success      | You are **authenticated** – your identity is confirmed                      |
| 4    | You choose "Withdraw ₹1000" | Authorization  | The system checks if you’re **allowed** to withdraw ₹1000 from your balance |

#### **Authentication vs Permission**

| Feature                  | **Authentication**                     | **Permission**                                  |
| ------------------------ | -------------------------------------- | ----------------------------------------------- |
| **Meaning**           | Proves **who you are**                 | Controls **what you can do**                    |
| **Example**           | Logging in with email and password     | Accessing admin panel, editing or deleting data |
| **When it happens**    | First step – before accessing anything | After authentication – to check access rights   |
| **Goal**              | Confirm identity                       | Grant or restrict actions                       |
| **Real-life analogy** | Showing your ID to enter a building    | Being allowed to enter certain rooms only       |

#### **Types of Authentication**
Basic Authentication, Token Authentication and JWT Authentication

## 1. Basic Authentication

How it works: Username and password are sent with every request, encoded in Base64.

Format:
Authorization: Basic <base64(username:password)>

Problem: Not secure unless using HTTPS. Password goes with every request.
```
<!-- Example: Login using curl: -->

curl -u username:password https://api.example.com/data
```

**Basic Authentication for the entire project (global) and for individual viewsets (class-based)**

Project structure
```
myproject/
├── blog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
```

models.py
```
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

serializers.py
```
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

views.py
```
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Optional: Use for per-class authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Enable basic auth only for this view
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
```

blog/urls.py
```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

myproject/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]
```

myproject/settings.py (Authentication Setup)
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'blog',
]

# Global authentication settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

```

2. Token Authentication

How it works: After login, the server gives a unique token. The client sends this token in every request.

Format:
Authorization: Token <token>

Example:
- You login → get abc123token
- Every request you send:
```
GET /data
Authorization: Token abc123token
```

3. JWT (JSON Web Token) Authentication

How it works:
- You log in → get a JWT token (a long string with 3 parts).
- You send this token in every request to prove your identity.

Format:
Authorization: Bearer <jwt_token>

Self-contained: It has user info + expiry + signature.

Can be verified without querying the DB on each request.
```
xxxxx.yyyyy.zzzzz
(Header).(Payload).(Signature)
```
