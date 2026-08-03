from rest_framework import serializers
from tags.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class LanguageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStatus
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class BannerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerLocation
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class TargetAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetAudience
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class InformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformType
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by", "created_at", "updated_at")
