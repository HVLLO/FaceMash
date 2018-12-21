from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from .models import Post
from api.like.mixins import LikedMixin


class PostAPIViewSet(LikedMixin, ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
