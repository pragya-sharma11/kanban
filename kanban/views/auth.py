from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.signals import user_logged_in
from rest_framework import exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from relevvo import serializers


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny)

    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.POST)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if (
            get_user_model()
            .objects.filter(email=serializer.validated_data["email"])
            .exists()
        ):
            raise exceptions.APIException(
                "A user with that email already exists.", status.HTTP_409_CONFLICT
            )

        user = get_user_model().objects.create_user(**serializer.validated_data)
        token = RefreshToken.for_user(user).access_token
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(
            dict(token=str(token), data=serializers.UserSerializer(user).data)
        )


class LoginAPIView(APIView):
    permission_classes = (AllowAny)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, **serializer.validated_data)
        if not user:
            raise exceptions.NotAuthenticated("Email and password do not match.")

        token = RefreshToken.for_user(user).access_token
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(
            dict(token=str(token), data=serializers.UserSerializer(user).data)
        )
