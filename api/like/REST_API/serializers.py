from rest_framework import serializers

from api.account.models import User


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
