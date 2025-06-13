from rest_framework import serializers
from .models import Company, JobPosting, Application, Applicant

class CompanySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
        
    def validate(self, data):
        # Prevent same applicant from applying to the same job twice (already handled by unique_together, but just to show)
        if Application.objects.filter(applicant=data['applicant'], job=data['job']).exists():
            raise serializers.ValidationError("You have already applied to this job.")
        return data