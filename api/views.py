from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserProfileSerializer, PostSerializer
from post.models import Post


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserProfileSerializer


# TODO: API Views for Post
class CreatePostAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer


class UpdatePostAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class ListPostAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DetailPostAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)

        return Response(data=serializer.data)
