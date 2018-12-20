from rest_framework import serializers

from api.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body', 'likes',)
