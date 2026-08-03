from rest_framework import serializers
from tags.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "name"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "full_name"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "name"


class LanguageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStatus
        fields = "status"


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "year"


class BannerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerLocation
        fields = ['location', 'banner_name']


class TargetAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetAudience
        fields = "audience"


class InformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformType
        fields = "type"


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = "status"
