from rest_framework import serializers

from account.models import User
from post.models import Post, Like


class UserProfileSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined',
                  'first_name', 'last_name', 'username',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  'body')


class LikeSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField

    class Meta:
        model = Like
        fields = ('id', 'user', 'post',
                  'created')
