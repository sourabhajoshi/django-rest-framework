from rest_framework import serializers
from ..models.prescriptions import Medicine, Prescription

# Medicine reference data
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

# Prescription serializer with M2M field
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
