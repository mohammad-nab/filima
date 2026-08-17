import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Subscription(models.Model):
    subscription_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_type = models.CharField(blank=True, null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_created_by')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_updated_by')
    title = models.CharField(max_length=200)
    is_special = models.BooleanField(default=False)
    price = models.CharField(max_length=50)
    price_by_discount = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubscriptionConf(models.Model):
    subscription_conf_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_conf_created_by')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_conf_updated_by')
    status_type = models.CharField(blank=True, null=True, max_length=50)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubscriptionPayment(models.Model):
    subscription_payment_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_payment_customer')
    price = models.CharField(max_length=50)
    is_discount = models.BooleanField(default=False)
    type = models.CharField(blank=True, null=True, max_length=50)
    discount_amount = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_payment_created_by')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='subscription_payment_updated_by')
    is_deleted = models.BooleanField(default=False)


class Discount(models.Model):
    discount_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='discount_created_by')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='discount_updated_by')
    code = models.CharField(max_length=50)
    status_type = models.CharField(max_length=50)
    percentage = models.FloatField()
    max_use_limit = models.PositiveSmallIntegerField()
    hours_limit = models.PositiveSmallIntegerField()
    used_count = models.PositiveSmallIntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code
