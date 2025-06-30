
# Token Authentication 

Token Authentication is a way to identify and authenticate users using a unique key (called a token) instead of username-password for each API request.

Real-Time Example:

Imagine you're using a food delivery app:

- You log in once using your email & password → app gives you a token.
- Every time you check your orders, it sends this token behind the scenes.
- Server checks if the token is valid → if yes, it lets you access your data.

You don’t have to log in again and again for every request.

**What is a Token?**

A token is a long random string (like 9a9d3012733a4b27b2341e9abf6f71a2). It is stored in the server’s database. It is sent by the client in every request using headers.
```
Authorization: Token 9a9d3012733a4b27b2341e9abf6f71a2
```

**rest_framework.authtoken**

It's a built-in app in DRF that helps generate and manage tokens for each user.

It creates a table named authtoken_token in the database where it stores the token for each user.

```
<!-- Add to INSTALLED_APPS -->
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

<!-- Than migrate -->
python manage.py migrate

```
This will create a new table for tokens in your database.


