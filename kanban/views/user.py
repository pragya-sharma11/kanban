from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from kanban import models, serializers

class LoggedInUserAPIView(APIView):
    def get(self, request):
        return Response(dict(data=serializers.UserSerializer(request.user).data))

    def put(self, request):
        serializer = serializers.UpdateUserQuerySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        get_user_model().objects.filter(id=user.id).update(**serializer.validated_data)
        user.refresh_from_db()

        return Response(dict(data=serializers.UserSerializer(user).data))


class ChangePasswordAPIView(APIView):
    def post(self, request):
        serializer = serializers.ChangePasswordQuerySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response(dict(data=serializers.UserSerializer(user).data))