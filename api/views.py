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
    queryset = Post.objects.all()


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


# TODO: Create URL's for this class
class DeletePostAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()


#
# TODO: Create API For Likes, CREATE "CRUD"
class CreateLikeAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# TODO: This curl request for test auth API
"""
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImFkbWluQGdtYWlsLmNvbSIsImV4cCI6MTU0NDk5MTY5NCwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20ifQ.6eaOnDftRh8pTEnZPho4BTUA2fQnqocvqCBsXf7FaxU" http://localhost:8000/api/v1/list/post/
"""
