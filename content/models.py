import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from tags.models import Genre, Country, Actor, LanguageStatus


class Content(models.Model):
    content_uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    persian_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    summary = models.TextField()
    is_special_show = models.BooleanField(default=False)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    imdb_rate = models.FloatField()
    duration = models.IntegerField()
    age_rate = models.IntegerField()
    is_free = models.BooleanField(default=False)
    is_special_list = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_content', null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='updated_content', null=True)
    satisfaction_avg = models.FloatField(default=0)
    is_dubbed = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        INITIAL = "INITIAL", "Initial"

    status_type = models.CharField(choices=Status, default=Status.INITIAL, max_length=8)

    class Type(models.TextChoices):
        MOVIE = "M", "Movie"
        SERIES = "S", "Series"

    type = models.CharField(choices=Type, default=Type.MOVIE, max_length=1)

    def __str__(self):
        return self.english_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_name)

        super().save(*args, **kwargs)


class ContentGenre(models.Model):
    content_genre_uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_genres')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='content_genres')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_content_genre', null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='updated_content_genre', null=True)
    is_deleted = models.BooleanField(default=False)


class ProducerCountry(models.Model):
    producer_country_uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='content_countries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_producer_country', null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='updated_product_country', null=True)
    is_deleted = models.BooleanField(default=False)


class ContentActor(models.Model):
    content_actor_uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='content_actors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_actor', null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='updated_actor', null=True)
    is_deleted = models.BooleanField(default=False)


class ContentLanguageStatus(models.Model):
    language_status_uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_language_statuses')
    language_status = models.ForeignKey(LanguageStatus, on_delete=models.CASCADE, related_name='content_language_statuses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_language_status', null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='updated_language_status', null=True)
    is_deleted = models.BooleanField(default=False)

