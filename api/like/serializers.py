from rest_framework import serializers

from root.settings import AUTH_USER_MODEL


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = AUTH_USER_MODEL
        fields = ('username',
                  'full_name')

    def get_full_name(self, obj):
        return obj.get_full_name()
