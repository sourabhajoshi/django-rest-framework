from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Company, JobPosting, Applicant, Application
from .serializers import CompanySerailizer, JobPostingSerializer, ApplicantSerializer, ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend  # Import filter backend
from rest_framework.renderers import JSONRenderer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerailizer
    
    
    
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    
    # Enables search by job title and location
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location']
    
    # Enables search by job title and location
    ordering_fields = ['created_at'] # Allows ?ordering=created_at or ?ordering=-created_at
    
    
    
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    
    # Enables search by name or email
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']  # ?search=john
    
    
    
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    renderer_classes = [JSONRenderer]
    # Enable filtering by applicant, job, and status
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['applicant', 'job', 'status'] # ?applicant=1&job=2&status=submitted
     