import uuid
from django.db import models
from django.contrib.auth import get_user_model


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
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_content')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='updated_content')
    satisfaction_avg = models.FloatField(default=0)
    is_dubbed = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return self.english_name