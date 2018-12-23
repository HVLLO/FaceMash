from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.like import services
from api.like.REST_API.serializers import FanSerializer


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """
        likes 'obj'
        :return:
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """
        dislike 'obj'
        :return:
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """
        Get all user who liked 'obj'
        :return:
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)
