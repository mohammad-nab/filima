from rest_framework import serializers
from subscription.models import Subscription, SubscriptionConf
from django.db import transaction


class SubscriptionConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionConf
        fields = '__all__'
        read_only_fields = ('slug', 'created_at', 'updated_at', 'created_by', 'updated_by', 'is_deleted')


class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_conf = SubscriptionConfSerializer(write_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = ('slug', 'created_at', 'updated_at', 'created_by', 'updated_by', 'is_deleted')


    @transaction.atomic
    def create(self, validated_data):
        subscription_conf = validated_data.pop('subscription_conf')

        subscription = Subscription.objects.create(**validated_data)
        SubscriptionConf.objects.create(**subscription_conf)

        return subscription
