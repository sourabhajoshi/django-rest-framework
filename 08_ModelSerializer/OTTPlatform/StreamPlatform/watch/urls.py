from rest_framework.routers import DefaultRouter
from .views import WatchListViewSet, StreamPlatformViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'stream', StreamPlatformViewSet, basename='streamplatform')
router.register(r'watch', WatchListViewSet, basename='watchlist')

urlpatterns = [
    path('', include(router.urls))
]
