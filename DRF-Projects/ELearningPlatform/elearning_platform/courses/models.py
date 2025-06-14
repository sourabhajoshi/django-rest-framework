from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(Instructor, related_name="courses", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    enrolled_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student}-{self.course}"

class Lesson(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
