from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateField()
    
    #create method
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    #update method
    def update(self, instance, validated_data):
        self.title = validated_data.get('title', instance.title)
        self.author = validated_data.get('author', instance.author)
        self.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance