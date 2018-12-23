from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (CreateAPIView, UpdateAPIView,)

from api.account.REST_API.serializers import UserProfileSerializer


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

