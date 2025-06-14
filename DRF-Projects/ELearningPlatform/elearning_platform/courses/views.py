from django.shortcuts import render
from .models import Instructor, Course, Student, Enrollment, Lesson
from .serializers import InstructorSerailizer, CourseSerailizer, StudentSerializer, EnrollmentSerializer, LessonSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerailizer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerailizer
    
    # Enable filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title', 'created_at']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all() 
    serializer_class = EnrollmentSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
