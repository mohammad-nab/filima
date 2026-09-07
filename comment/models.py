import uuid
from django.db import models
from content.models import Content
from accounts.models import Customer


class Comment(models.Model):
    comment_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        INITIAL = "INITIAL", "Initial"

    status_type = models.CharField(choices=Status, default=Status.INITIAL, max_length=10)
    is_deleted = models.BooleanField(default=False)