from rest_framework import serializers

from api.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body', 'total_likes')
