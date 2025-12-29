# Django Relationships

A relationship is a connection between two data entities. These relationships help represent real-world associations like:

- A person has one passport.
- A teacher teaches many students.
- A student can enroll in many courses, and each course can have many students.

### **Types of Relationships**
There are three main types of relationships: One-to-One, One-to-Many and Many-to-Many

**1. One-to-One (1:1)**

One record in a table is associated with exactly one record in another table.

ಒಂದು model ನಲ್ಲಿ ಒಂದು record → ಇನ್ನೊಂದು model ನಲ್ಲಿ ಒಂದು record ಗೆ ಮಾತ್ರ connect ಆಗಿರುತ್ತದೆ.

Example:
- One person has one passport.
- One user has one profile.

```
class User(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```
Two entities have a strict 1:1 mapping.

You want to split data into related tables for organizational or performance reasons.

**2. One-to-Many (1:N)**

One record in a table is associated with multiple records in another table.

ಒಂದು ಟೇಬಲ್‌ನ ಒಂದು ದಾಖಲೆ (record) ಇನ್ನೊಂದು ಟೇಬಲ್‌ನ ಅನೇಕ ದಾಖಲೆಗಳಿಗೆ ಸಂಬಂಧ ಹೊಂದಿರುತ್ತದೆ. Django ನಲ್ಲಿ ಇದನ್ನು ForeignKey ಉಪಯೋಗಿಸಿ ರಚಿಸಲಾಗುತ್ತದೆ.

Example:
- One author writes many books.
- One department has many employees.

```
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```
A parent object can have multiple child objects, but each child belongs to only one parent.

```
class Blog(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```
Blog = One, Posts = Many

**3. Many-to-Many (M:N)**

Multiple records in one table are associated with multiple records in another table.

Many-to-Many ಸಂಬಂಧ ಅಂದರೆ ಒಂದು ಟೇಬಲ್‌ನಲ್ಲಿ ಅನೇಕ ದಾಖಲೆಗಳು ಇನ್ನೊಂದು ಟೇಬಲ್‌ನ ಅನೇಕ ದಾಖಲೆಗಳಿಗೆ ಸಂಬಂಧ ಹೊಂದಿರಬಹುದು.
- ಒಬ್ಬ ವಿದ್ಯಾರ್ಥಿ ಅನೇಕ ಕೋರ್ಸ್ ಪಡೆಯಬಹುದು
- ಒಂದೇ ಕೋರ್ಸ್‌ಗೆ ಅನೇಕ ವಿದ್ಯಾರ್ಥಿಗಳು ಇರಬಹುದು

Example:
- Students enroll in many courses, and each course has many students.
- Movies have many actors, and actors act in many movies.
```
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```
You need a bidirectional and multi-linked relationship.

Django will create an intermediate table behind the scenes to store the links.
