from rest_framework import viewsets
from ..models.user_profile import DoctorProfile, PatientProfile
from ..searializers.user_profiles import DoctorSerializer, PatientProfileSerializer

# CRUD for doctors
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer

# CRUD for patients
class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
