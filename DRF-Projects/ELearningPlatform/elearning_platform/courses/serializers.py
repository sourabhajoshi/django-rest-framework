from rest_framework import serializers
from .models import Instructor, Course, Student, Enrollment, Lesson

class InstructorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseSerailizer(serializers.ModelSerializer):
    
    instructor = InstructorSerailizer(read_only = True)
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    
    student = StudentSerializer(read_only=True)
    course = CourseSerailizer(read_only=True)
    
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'