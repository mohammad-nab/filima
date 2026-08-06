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

    def validate_full_name(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("An actor with this name already exists.")
        return value

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_name(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A country with this name already exists.")
        return value


class LanguageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStatus
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_status(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A language with this status already exists.")
        return value

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_year(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A year with this number already exists.")
        return value




class BannerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerLocation
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

        def validate(self, attrs):
            banner_name = attrs.get("banner_name")
            location = attrs.get("location")

            qs = BannerLocation.objects.filter(
                banner_name__iexact=banner_name,
                location__iexact=location,
            )

            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "A banner with this name and location already exists."
                )

            return attrs


class TargetAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetAudience
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_audience(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A audience with this name already exists.")
        return value


class InformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformType
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_type(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A inform with this type already exists.")
        return value


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = "__all__"
        read_only_fields = ("slug", "created_by", "updated_by", "created_at", "updated_at")

    def validate_status(self, value):
        value = value.strip()
        qs = Actor.objects.filter(full_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A status with this name already exists.")
        return value
