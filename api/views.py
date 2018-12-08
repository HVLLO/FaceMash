from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


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

    authenticated_jwt(email, password)
