from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Post

from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer 

class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


