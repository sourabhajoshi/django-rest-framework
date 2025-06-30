from rest_framework import serializers
from ..models.appointments import Appointment

# Serialize Appointment details
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
