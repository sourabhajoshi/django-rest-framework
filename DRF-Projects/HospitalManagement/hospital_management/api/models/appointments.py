from django.db import models
from .user_profile import DoctorProfile, PatientProfile


# Appointment links a doctor and a patient at a specific time
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    symptoms = models.TextField()
    
    