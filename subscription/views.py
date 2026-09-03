from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from conf.pagination import CustomPagination
from .models import Subscription, Discount
from rest_framework.response import Response
from .serializers import SubscriptionSerializer, DiscountSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import random
import string


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAdminUser]

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


class CreateRandomDiscountCodeView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        length = 8
        while True:

            code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

            if not Discount.objects.filter(code=code).exists():
                break

        return Response({'code': code})


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.filter(is_deleted=False)
    serializer_class = DiscountSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status_type']
    search_fields = ['code']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_instance.is_deleted = True
        old_instance.save(update_fields=['is_deleted'])

        data = {
            'code': old_instance.code,
            'status_type': old_instance.status_type,
            'percentage': old_instance.percentage,
            'max_use_limit': old_instance.max_use_limit,
            'hours_limit': old_instance.hours_limit,
            **serializer.validated_data,
        }

        new_instance = Discount.objects.create(
            **data,
            created_by=old_instance.created_by,
            updated_by=self.request.user,
            is_deleted=False,
        )
        serializer.instance = new_instance

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save(update_fields=['is_deleted'])
