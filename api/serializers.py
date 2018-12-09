from rest_framework import serializers

from account.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField

    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
