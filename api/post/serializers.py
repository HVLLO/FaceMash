from rest_framework import serializers

from api.post.models import Post
import api.like.services as likes_services


class PostSerializer(serializers.ModelSerializer):
    # is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body', 'total_likes', )

    # def get_is_fun(self, obj) -> bool:
    #     """
    #     Check, request.user liked post (obj)
    #     :param obj:
    #     :return: bool
    #     """
    #     user = self.context.get('request').user
    #     return likes_services.is_fan(obj, user)
