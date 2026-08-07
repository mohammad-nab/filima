from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = [
            "slug",
            "customer_uuid",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'username', 'first_name', 'last_name', 'email',
                  'is_subscribe', 'subscription_start_date', 'subscription_type']

        read_only_fields = ("slug", 'phone_number', 'is_subscribe', 'subscription_start_date', 'subscription_type')


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = get_user_model()
        fields = ('phone_number', 'username', 'first_name', 'last_name', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('password2')
        return get_user_model().objects.create_user(**validated_data)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=11)

class CheckOTPSerializer(serializers.Serializer):
    otp_code = serializers.CharField(required=True, max_length=6)
    phone_number = serializers.CharField(required=True, max_length=11)


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)