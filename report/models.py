import uuid
from django.db import models
from django.contrib.auth import get_user_model
from content.models import Content



class LikeDislike(models.Model):
    like_dislike_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
    is_like = models.BooleanField()
    is_dislike = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(f"{self.content} - {self.customer}")