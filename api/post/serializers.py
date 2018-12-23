from rest_framework import serializers

from api.post.models import Post
import api.like.services as likes_services


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body',)
