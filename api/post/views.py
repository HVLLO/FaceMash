from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post
from api.like.mixins import LikedMixin


class PostAPIViewSet(LikedMixin,
                     viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

