from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from api.post.REST_API.serializers import PostSerializer
from api.post.models import Post
from api.like.REST_API.mixins import LikedMixin


class PostAPIViewSet(LikedMixin,
                     viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
