from rest_framework import serializers
from .models import Content, ContentGenre, ContentActor, ProducerCountry, ContentLanguageStatus
from tags.models import Genre, Actor, Country, LanguageStatus
from django.db import transaction


class ContentSerializer(serializers.ModelSerializer):

    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
    )

    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )

    countries = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        many=True,
    )

    language_statuses = serializers.PrimaryKeyRelatedField(
        queryset=LanguageStatus.objects.all(),
        many=True,
    )

    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ["slug", "content_uuid", "created_at", "updated_at", "created_by", "updated_by"]

    @transaction.atomic
    def create(self, validated_data):
        genres = validated_data.pop("genres")
        actors = validated_data.pop("actors")
        countries = validated_data.pop("countries")
        language_statuses = validated_data.pop("language_statuses")

        user = self.context["request"].user

        content = Content.objects.create(
            **validated_data
        )

        ContentGenre.objects.bulk_create([
            ContentGenre(
                content=content,
                genre=genre,
                created_by=user,
                updated_by=user,
            )
            for genre in genres
        ])

        ContentActor.objects.bulk_create([
            ContentActor(
                content=content,
                actor=actor,
                created_by=user,
                updated_by=user,
            )
            for actor in actors
        ])

        ProducerCountry.objects.bulk_create([
            ProducerCountry(
                content=content,
                country=country,
                created_by=user,
                updated_by=user,
            )
            for country in countries
        ])

        ContentLanguageStatus.objects.bulk_create([
            ContentLanguageStatus(
                content=content,
                language_status=language_status,
                created_by=user,
                updated_by=user,
            )
            for language_status in language_statuses
        ])

        return content