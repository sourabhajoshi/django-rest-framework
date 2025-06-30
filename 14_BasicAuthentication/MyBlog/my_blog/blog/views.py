from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
# Optional: Use for per-class authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
