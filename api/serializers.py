from rest_framework import serializers

from account.models import User
from post.models import Post, Like


class UserProfileSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class PostSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ('id', 'user', 'title',
                  'body')
