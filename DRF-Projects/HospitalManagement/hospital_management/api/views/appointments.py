from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
from ..models.appointments import Appointment
from ..searializers.appointments import AppointmentSerializer

# Allows filtering by doctor or date, and search by names
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer