import uuid
from django.db import models
from django.conf import settings
from django.db.models.functions import Lower
from django.utils.text import slugify


class Genre(models.Model):
    genre_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='create_genres')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='update_genres')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_genre_name_case_insensitive",
            )
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Actor(models.Model):
    actor_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_actor')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_actor')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("full_name"),
                name="unique_actor_name_case_insensitive",
            )
        ]

    def __str__(self):
        return self.full_name

class Country(models.Model):
    country_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_country')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_country')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_country_name_case_insensitive",
            )
        ]

    def __str__(self):
        return self.name


class Year(models.Model):
    year_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_year')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_year')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("year"),
                name="unique_year_case_insensitive",
            )
        ]

    def __str__(self):
        return self.year


class LanguageStatus(models.Model):
    language_status_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_language')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_language')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("status"),
                name="unique_language_status_case_insensitive",
            )
        ]

    def __str__(self):
        return self.status


class BannerLocation(models.Model):
    banner_location_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    banner_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_location')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_location')
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('banner_name'),
                Lower('location'),
                name='unique_banner_name_location_case_insensitive',
            )
        ]

    def __str__(self):
        return f"{self.banner_name} - {self.location}"


class TargetAudience(models.Model):
    target_audience_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    audience = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_audience')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_audience')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("audience"),
                name="unique_target_audience_case_insensitive",
            )
        ]

    def __str__(self):
        return self.audience


class InformType(models.Model):
    inform_type_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_type')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_type')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("type"),
                name="unique_inform_type_case_insensitive",
            )
        ]

    def __str__(self):
        return self.type


class AccountStatus(models.Model):
    account_status_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='create_account_status')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='update_account_status')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("status"),
                name="unique_account_status_case_insensitive",
            )
        ]

    def __str__(self):
        return self.status
