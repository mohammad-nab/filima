from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from .serializers import (UserRegisterSerializer, UserLoginSerializer,
                          CheckOTPSerializer, UserSerializer, UserSelfSerializer, UserLogoutSerializer)
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from utils import send_otp_code
from rest_framework_simplejwt.tokens import RefreshToken
import secrets
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .redis_client import save_otp, get_otp, delete_otp, can_request_otp, increase_attempt, delete_attempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['status_type']
    search_fields = ['phone_number']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_update(self, serializer):
            serializer.save(updated_by=self.request.user)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSelfSerializer

    def get_object(self):
        return self.request.user


class UserRegistrationView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        customer = get_object_or_404(get_user_model(), phone_number=phone_number)
        if not can_request_otp(phone_number):
            return Response({"message": "Please wait 60 seconds before requesting another OTP."},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        otp_code = str(secrets.randbelow(900000) + 100000)
        save_otp(phone_number, otp_code)
        try:
            send_otp_code(code=otp_code)
            return Response({"message": "otp sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            delete_otp(phone_number)
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckOTPCodeView(APIView):
    serializer_class = CheckOTPSerializer
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data['otp_code']
        phone_number = serializer.validated_data['phone_number']

        real_otp = get_otp(phone_number)

        if real_otp is None:
            return Response({"message": "OTP has expired or does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        elif real_otp != otp_code:
            attempts = increase_attempt(phone_number)

            if attempts >= 5 :
                delete_otp(phone_number)
                delete_attempt(f"otp_attempts:{phone_number}")
                return Response({"message": "Too many attempts. Please request a new OTP."},
                                status=status.HTTP_429_TOO_MANY_REQUESTS
                                )

            return Response({"message": "Wrong OTP."}, status=status.HTTP_400_BAD_REQUEST)

        delete_otp(phone_number)
        delete_attempt(f"otp_attempts:{phone_number}")
        customer = get_object_or_404(get_user_model(), phone_number=phone_number)
        refresh = RefreshToken.for_user(customer)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)},
            status=status.HTTP_200_OK
        )


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
        except TokenError:
            return Response(
                {"detail": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)