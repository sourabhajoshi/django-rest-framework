from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    # field-level validation for title
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Title should be at least 5 char long.')
        return value
    
    class Meta: 
        model = Task
        # Include only specific fields
        fields = ['id', 'title', 'due_date', 'is_complete']

        # OR: To include all fields
        # fields = '__all__'

        # OR: To exclude specific fields
        # exclude = ['description']
