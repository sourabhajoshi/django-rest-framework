from rest_framework import serializers
from ..models.diseases import Disease, PatientDisease

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'
        
        
# Links patients and diseases (ManyToMany via FK)
class PatientDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDisease
        fields = '__all__'