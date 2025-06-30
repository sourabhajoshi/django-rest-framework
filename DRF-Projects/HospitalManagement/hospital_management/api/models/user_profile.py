from django.db import models
from django.contrib.auth.models import User

# Each doctor is associated with exactly one user
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 1-1 with User
    specialization = models.CharField(max_length=100)           # e.g., Cardiologist
    department = models.CharField(max_length=100)               # e.g., Cardiology
    
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()