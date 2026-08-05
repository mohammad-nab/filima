from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from tags.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_name(self, value):
        value = value.strip()
        qs = Genre.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A genre with this name already exists.")
        return value


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class LanguageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStatus
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class BannerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerLocation
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class TargetAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetAudience
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class InformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformType
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")
