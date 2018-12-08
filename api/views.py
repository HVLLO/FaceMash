from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from .serializers import UserProfileSerializer
from .utils import authenticated_jwt


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
