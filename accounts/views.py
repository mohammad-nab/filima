from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response


class UserRegistrationView(APIView):
    def post(self, request):
        ser_data = UserSerializer(data=request.data)

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


