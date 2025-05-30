# Django Rest Framework

Django REST Framework (DRF) is a powerful library built on top of Django that helps you create RESTful APIs easily.

DRF helps you convert your Django models and views into API endpoints that return data in JSON format — perfect for mobile apps, frontend frameworks (like React/Vue), or any external service.

**Why Use DRF?**

* Easy to build APIs for frontend apps (React, Vue, etc.)
* Supports authentication, permissions, filtering, pagination
* Clean, modular, and secure

Official document : https://www.django-rest-framework.org/

### **Step-by-Step Installation Process of DRF**

Step 1: Install Django
```
pip install django
```

Step 2: Create a Django project
```
django-admin startproject myproject
cd myproject
```

Step 3: Create an app (e.g., movies)
```
python manage.py startapp movies
```

Step 4: Install Django REST Framework
```
pip install djangorestframework
```

Step 5: Add 'rest_framework' to INSTALLED_APPS in settings.py
```
# myproject/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',   # Add this
    'movies',           # Your app
]
```

### **api/ folder**

In a Django + Django REST Framework (DRF) project, creating an api/ folder (or package) is not required, but it is considered a good practice in larger or well-structured projects.

A typical Django app has this structure:
```
myapp/
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py
├── serializers.py
├── tests.py
```
But when you start separating logic for API endpoints (especially with DRF), your app can look like this:
```
myapp/
├── api/
│   ├── __init__.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── permissions.py
├── models.py
├── admin.py
├── apps.py
├── tests.py
```
In huge projects, you can go even further:
```
myapp/
├── api/
│   ├── v1/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── permissions.py
│   └── v2/   # for future API versioning
├── models.py
...
```

Reason/Benifits to use api/ : 

* Separate API logic	: Cleaner organization
* Scalability : Easier to manage multiple views
* DRF best practices : Helps structure serializers/views
* Versioning ready : Easy to support v1, v2, etc.
