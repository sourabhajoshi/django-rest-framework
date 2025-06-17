# Scenario: Library Management System - Book Catalog

- Store book records (title, author, ISBN, publication date, genre).
- Allow users to fetch a list of books.
- The book list must be paginated, showing 5 books per page.

| Feature              | DRF Concept Used       |
| -------------------- | ---------------------- |
| Store book data      | Django `Model`         |
| Serialize book data  | `ModelSerializer`      |
| Expose API endpoints | `ViewSet` with Router  |
| Paginate book list   | `PageNumberPagination` |


You can access:
- /api/books/?page=1
- /api/books/?page=2
- /api/books/?page=1&page_size=10

Filtering
- GET /api/books/?genre=Fantasy
- GET /api/books/?author=Agatha Christie

Searching
- GET /api/books/?search=tolkien

Ordering
- GET /api/books/?ordering=publication_date
- GET /api/books/?ordering=-title (descending)

Pagination (still works)
- GET /api/books/?page=2