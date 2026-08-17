from rest_framework import serializers
from .models import Content, ContentGenre, ContentActor, ProducerCountry, ContentLanguageStatus
from tags.models import Genre, Actor, Country, LanguageStatus
from django.db import transaction


class ContentSerializer(serializers.ModelSerializer):

    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
    )

    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
        write_only=True,
    )

    countries = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        many=True,
        write_only=True,
    )

    language_statuses = serializers.PrimaryKeyRelatedField(
        queryset=LanguageStatus.objects.all(),
        many=True,
        write_only=True,
    )

    genre_ids = serializers.SerializerMethodField()
    actor_ids = serializers.SerializerMethodField()
    country_ids = serializers.SerializerMethodField()
    language_status_ids = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ["slug", "content_uuid", "created_at", "updated_at", "created_by", "updated_by"]

    def get_genre_ids(self, obj):
        return list(
            obj.content_genres.filter(is_deleted=False).values_list("genre_id", flat=True)
        )

    def get_actor_ids(self, obj):
        return list(
            obj.content_actors.filter(is_deleted=False).values_list("actor_id", flat=True)
        )

    def get_country_ids(self, obj):
        return list(
            obj.content_countries.filter(is_deleted=False).values_list("country_id", flat=True)
        )

    def get_language_status_ids(self, obj):
        return list(
            obj.content_language_statuses.filter(is_deleted=False).values_list("language_status_id", flat=True)
        )


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