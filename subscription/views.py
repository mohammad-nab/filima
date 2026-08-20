from rest_framework import viewsets
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_instance.is_deleted = True
        old_instance.save(update_fields=['is_deleted'])

        data = {
            "status_type": old_instance.status_type,
            "title": old_instance.title,
            "price": old_instance.price,
            "price_by_discount": old_instance.price_by_discount,
        }

        data.update(serializer.validated_data)

        new_instance = Subscription.objects.create(
            **data,
            created_by=self.request.user,
            updated_by=self.request.user,
        )
        serializer.instance = new_instance


