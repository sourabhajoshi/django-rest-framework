# Permission in DRF 

Permissions in DRF are used to control access to views and protect your API.

They apply:
- Globally (via settings)
- Per-view or viewset (per class/function)
- Per object (fine-grained control)

### **Global Permissions via Settings**

You can set a default permission policy in settings.py, which applies to all API views unless explicitly overridden.
```
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Global default
    ]
}
```
With the above, every API view requires login (authenticated user).

### **Built-in DRF Permission Classes**

**AllowAny**

Allows unrestricted access to any user — even anonymous. Useful for public pages like registration, home, etc.
```
from rest_framework.permissions import AllowAny

class PublicView(APIView):
    permission_classes = [AllowAny]
```

**IsAuthenticated**

Allows access only to authenticated users (logged in). Requires login (via session, token, or JWT).
```
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
```

**IsAdminUser**

Allows access only to admin users (is_staff=True in Django). Useful for admin dashboards or control panels.
```
from rest_framework.permissions import IsAdminUser

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]
```

**IsAuthenticatedOrReadOnly**

- Unauthenticated users: can only read (GET, HEAD, OPTIONS)

- Authenticated users: can read and write

Common for public blogs, course listings, etc.
```
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MixedAccessView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
```

| Permission                  | Who Can Access?                           | Typical Use           |
| --------------------------- | ----------------------------------------- | --------------------- |
| `AllowAny`                  | Everyone                                  | Public pages          |
| `IsAuthenticated`           | Only logged-in users                      | User dashboards       |
| `IsAdminUser`               | Only staff/admins                         | Admin API             |
| `IsAuthenticatedOrReadOnly` | Anyone can read; only logged-in can write | Public APIs with auth |


### **Using Permissions in Views**

**Class-Based Views (CBV)**
```
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

**Function-Based Views (FBV)**
```
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_view(request):
    return Response({"message": "Hello, authenticated user!"})
```
