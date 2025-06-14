# E-Learning Platform

Key Entities (Models):
- Instructor
- Course (created by an instructor)
- Student
- Enrollment (student enrolls in a course)
- Lesson (part of a course)

```
+------------------+
|  Instructor      |
+------------------+
| id: int          |
| name: str        |
| email: str       |
+------------------+
         |
         | 1
         | 
         | *
+------------------+
|  Course          |
+------------------+
| id: int          |
| title: str       |
| description: str |
| created_at: date |
| instructor_id: FK|
+------------------+
         |
         | 1
         |
         | *
+------------------+
|   Lesson         |
+------------------+
| id: int          |
| title: str       |
| content: text    |
| course_id: FK    |
+------------------+

+------------------+
|  Student         |
+------------------+
| id: int          |
| name: str        |
| email: str       |
+------------------+
         ^
         |
         | *
         |
         | 1
+------------------+
|  Enrollment      |
+------------------+
| id: int          |
| enrolled_at: dt  |
| student_id: FK   |
| course_id: FK    |
+------------------+

```
