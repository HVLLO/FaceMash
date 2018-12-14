from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from .serializers import UserProfileSerializer, PostSerializer
from .utils import authenticated_jwt

from post.models import Post


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserProfileSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def auth_user(request):
    email = request.data['email']
    password = request.data['password']
    auth = authenticated_jwt(email, password, request)

    return Response(auth, status=HTTP_200_OK)


# TODO: API Views for Post
class CreatePostAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer


class UpdatePostAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer


class ListPostAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer


class DetailPostAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)

        return Response(data=serializer.data)
