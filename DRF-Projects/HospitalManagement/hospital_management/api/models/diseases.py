from django.db import models
from .user_profile import PatientProfile

# A predefined list of diseases, used as reference data
class Disease(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    


# ManyToMany: Each patient can have many diseases and vice versa
class PatientDisease(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    diagnosed_on = models.DateField()    