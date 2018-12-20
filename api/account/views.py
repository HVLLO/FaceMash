from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (CreateAPIView, UpdateAPIView,)

from .serializers import UserProfileSerializer
from .models import User


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer


# TODO: Check UpdateAPIView
# TODO: Expected view UpdateUserAPIView to be called with a URL keyword argument named "pk"
class UpdateUserAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
