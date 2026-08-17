from rest_framework import serializers
from image.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ['image_uuid', 'created_by', 'updated_by', 'is_deleted', 'created_at', 'updated_at']