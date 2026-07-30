from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.CharField(max_length=200)

    def __str__(self):
        return self.year


class LanguageStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status


class BannerLocation(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location


class TargetAudience(models.Model):
    target = models.CharField(max_length=200)

    def __str__(self):
        return self.target


class InformType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class AccountStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status