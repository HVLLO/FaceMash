from rest_framework import serializers

from api.post.models import Post

from api.like import services as like_service


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body', 'is_fan', 'total_likes')

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return like_service.is_fan(obj, user)

