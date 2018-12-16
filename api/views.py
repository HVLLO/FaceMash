from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserProfileSerializer, PostSerializer
from post.models import Post


# API For User
class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer


class UpdateUserAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer


# API Views for Post
class CreatePostAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer


class UpdatePostAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class ListPostAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DetailPostAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)

        return Response(data=serializer.data)


"""
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImFkbWluQGdtYWlsLmNvbSIsImV4cCI6MTU0NDk4NDM2NiwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20ifQ.NMPHAYv1khEJfH5eC-88G36jX9r7iGbcjQzvZI5NPTI" http://localhost:8000/api/v1/list/post/
"""
