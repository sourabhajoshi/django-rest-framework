from rest_framework import serializers
from .models import StreamPlatform, WatchList

# Serializewr for watchlist model
class WatchListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__" # we can also create list fields manually like ['id', 'title', 'platform']
        

class StreamPlatformSerializer(serializers.ModelSerializer):
    # Show related watchlist items as nested objects
    watchList = WatchListSerailizer(many=True, read_only = True) 
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"