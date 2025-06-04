from rest_framework import serializers
from .models import Movie

# serializers.Serializer : manually define each field
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length = 50)
    genre = serializers.CharField(max_length=25)
    release_year = serializers.IntegerField()
    rating = serializers.FloatField()
    
    #create a method : create a new movie
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    #Update method
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
        