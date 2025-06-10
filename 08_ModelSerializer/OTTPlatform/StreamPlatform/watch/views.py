from rest_framework import viewsets
from .models import StreamPlatform, WatchList
from .serializers import StreamPlatformSerializer, WatchListSerailizer

class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerailizer
    