from rest_framework import serializers
from ..models.user_profile import PatientProfile, DoctorProfile
from django.contrib.auth.models import User

# Serializer for Django's built-in User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() # Nested serialization
    
    class meta:
        model = PatientProfile
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serialization

    class Meta:
        model = DoctorProfile
        fields = '__all__'
