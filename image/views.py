from rest_framework import viewsets
from image.models import Image
from image.serializers import ImageSerializer
from rest_framework.permissions import IsAdminUser


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Image.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_instance.is_deleted = True
        old_instance.save(update_fields=['is_deleted'])

        new_instance = Image.objects.create(
            content=old_instance.content,
            created_by=old_instance.created_by,
            updated_by=self.request.user,
            is_deleted=False,
            **serializer.validated_data
        )
        serializer.instance = new_instance