from django.contrib.auth import get_user_model
from rest_framework import serializers


class UpdateUserQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class ChangePasswordQuerySerializer(serializers.Serializer):
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password',)
