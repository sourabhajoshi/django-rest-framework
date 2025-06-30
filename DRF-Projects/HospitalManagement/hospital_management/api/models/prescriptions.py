from django.db import models
from .appointments import Appointment

# Medicine master table, used in prescriptions
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    dosage_info = models.CharField(max_length=255)
    

# Prescription links an appointment with multiple medicines
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # Issued for this appointment
    prescribed_on = models.DateField(auto_now_add=True)                     # Automatically set to today
    medicines = models.ManyToManyField(Medicine)                            # Prescribed medicines
    notes = models.TextField(blank=True, null=True)                         # Optional doctor comments
