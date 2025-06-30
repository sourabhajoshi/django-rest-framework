from rest_framework import viewsets
from ..models.diseases import Disease, PatientDisease
from ..searializers.diseases import DiseaseSerializer, PatientDiseaseSerializer

# Viewset for disease master data
class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

# Viewset for linking patients and diseases
class PatientDiseaseViewSet(viewsets.ModelViewSet):
    queryset = PatientDisease.objects.all()
    serializer_class = PatientDiseaseSerializer
