from rest_framework import serializers

from api.account.models import User


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

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
