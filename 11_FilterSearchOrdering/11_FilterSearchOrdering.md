# Filterning in DRF

Filtering in DRF allows users to narrow down the results of a query by adding parameters to the URL.
```
GET /api/books/?author=3 

# This will return only the books where author has the ID 3.
```

**Why Use Filtering**
- Makes your API more dynamic and useful.
- Reduces the need for multiple hard-coded endpoints.
- Enables frontend and mobile apps to fetch filtered data easily.

Let’s assume you already have a Book model with a foreign key to an Author.

Step 1 : Install django-filter

This is an external package used for filtering in DRF.
```
pip install django-filter
```

Step 2 : Add django_filters to INSTALLED_APPS
```
INSTALLED_APPS = [
    ...
    'django_filters',  # Needed for DjangoFilterBackend to work
]
```

Step 3: Configure DRF to Use Filtering Backend
```
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',  # Enables filtering support
    ]
}

# This tells DRF: "Use this backend whenever a view supports filtering."
```

Step 4: Update Your ViewSet
```
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # This enables filtering in this ViewSet
    filter_backends = [DjangoFilterBackend]

    # These are the model fields that can be filtered via URL query params
    filterset_fields = ['author', 'title']
```

**What Happens Behind the Scenes?**
- DjangoFilterBackend reads filterset_fields.
- It looks for query params that match the listed fields.
- If it finds them, it applies .filter() on the queryset.

**Important Notes to Remember**

1. filterset_fields must match actual model field names
- You can filter by ForeignKey fields (like author) using their ID.
- Example: author=1 not author=John.

2. Only listed fields are filterable
```
filterset_fields = ['title', 'author']

# /api/books/?price=20 → will NOT work if price isn't listed.
```

3. You can filter on related fields
For example, if Book has a foreign key to Author, and Author has a name field, you can do
```
filterset_fields = ['author__name']


Than call

/api/books/?author__name=William #This is very useful for nested relationships.
```

4. You can use custom lookup expressions
```
filterset_fields = {
    'title': ['exact', 'icontains', 'startswith'],
    'author': ['exact'],
}

Now you can do:

/api/books/?title__icontains=django → case-insensitive contains
/api/books/?title__startswith=Django
```

# Filterning in DRF

Searching allows API users to find records based on keywords across one or more fields — such as a book's title or its author's name.

```
GET /api/books/?search=django
```
Returns all books where the title or author's name contains the word "django" (case-insensitive).

Why Use Searching?
- Flexible and user-friendly.
- Great for global keyword lookups.
- Essential for search bars, autocomplete, and admin filtering.


Step 1: Add SearchFilter to Your Project

You don’t need to install anything extra. SearchFilter is included in DRF by default.

Just add it to your REST framework config or view.

Step 1 : Global setup in settings.py
```
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
    ]
}

```

Step 2: Use per ViewSet (Recommended)
```
# books/views.py

from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enables search functionality
    filter_backends = [filters.SearchFilter]

    # Fields you want to enable for search
    search_fields = ['title', 'author__name']
```

How it works?
```
GET /api/books/?search=django

DRF will automatically apply the icontains lookup on both:
* Book.title
* Author.name (via author__name)
```

Important Notes and Tips
1. Uses icontains by default
Case-insensitive, Partial matches allowed

Search is not tokenized like a full-text search engine

2. Works with Foreign Key fields using __
You can search by related fields like author__name

3. search_fields must list valid fields
DRF will raise an error if the field doesn’t exist

Related fields (author__name) work only if related model has a __str__() method

# Ordering in DRF

Ordering allows users to sort API results based on one or more fields.
```
GET /api/books/?ordering=title # This will return books ordered alphabetically by title (A to Z).

GET /api/books/?ordering=-id # Adds a minus (-) to sort in descending order by ID.

```

Why Use Ordering?
- Useful for listing newest or oldest items.
- Helps users sort alphabetically, by price, by date, etc.
- Supports multiple field sorting.

Step 1: No extra installation needed

Ordering support is already built into DRF using OrderingFilter.

Step 2: Add OrderingFilter Globally (Optional)
```
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
    ]
}
```

Step 3: Use OrderingFilter in Your ViewSet
```
# views.py

from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enables ordering
    filter_backends = [filters.OrderingFilter]

    # Users can sort by these fields via ?ordering=field
    ordering_fields = ['title', 'id']

    # 🔧 Default ordering (if no ordering param is passed)
    ordering = ['id']
```

----
