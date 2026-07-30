import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomerManager



class Customer(AbstractBaseUser):
    customer_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    objects = CustomerManager()

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', "Active"
        INACTIVE = "INACTIVE", "Inactive"

    status_type = models.CharField(
        max_length=8,
        choices=Status,
        default=Status.INACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_subscribe = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)
    subscription_count = models.IntegerField(default=0)
    subscription_start_date = models.DateTimeField(null=True, blank=True)

    class SubscriptionType(models.IntegerChoices):
        ONE = 1 , "One month"
        THREE = 3, "Three months"
        SIX = 6, "Six months",
        TWELVE = 12, "Twelve months"

    subscription_type = models.CharField(
        max_length=8,
        choices=SubscriptionType,
        blank=True,
        null=True
    )
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    active_device_count = models.IntegerField(default=0)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin