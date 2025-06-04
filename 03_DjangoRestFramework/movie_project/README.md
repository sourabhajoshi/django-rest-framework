# Movie API – Django REST Framework Project

A simple RESTful API built using **Django** and **Django REST Framework** to manage a collection of movies. This API supports full **CRUD operations** – Create, Read, Update, and Delete movie records.
---

## Features

- Add new movies
- List all movies
- View a single movie by ID
- Update movie details
- Delete a movie
- Uses manual `serializers.Serializer` for full control

---

## Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Database**: SQLite (default, easy setup)
- **API Format**: JSON
- **Tools**: `@api_view`, `serializers.Serializer`, `Response`, `status`

---

## Folder Structure
```
movie_project/
│
├── movie_app/
│ ├── migrations/
│ ├── init.py
│ ├── models.py # Movie model
│ ├── serializers.py # Manual serializer for Movie
│ ├── views.py # API logic (GET, POST, PUT, DELETE)
│ └── urls.py # API endpoints
│
├── movie_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py # Root URL config
│ └── wsgi.py
│
├── manage.py
└── db.sqlite3
```

```
## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Setup Instructions

```
# Step 1: Clone the repo
git clone https://github.com/sourabhajoshi/django-rest-framework/tree/main/03_DjangoRestFramework/movie_project/movie-api-drf.git
cd movie-api-drf

# Step 2: Create and activate a virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# Step 3: Install dependencies
pip install django djangorestframework

# Step 4: Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Step 5: Run the server
python manage.py runserver
```

