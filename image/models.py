import uuid
from django.db import models
from content.models import Content
from django.contrib.auth import get_user_model
from django.db.models.functions import Lower



class Image(models.Model):
    image_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='created_image')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='updated_image')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('content'),
                Lower('image_type'),
                condition= models.Q(is_deleted=False),
                name='unique_active_image_per_type'
            )
        ]

