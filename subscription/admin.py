from django.contrib import admin
from subscription.models import Subscription, SubscriptionConf, SubscriptionPayment, Discount


admin.site.register(Subscription)
admin.site.register(SubscriptionConf)
admin.site.register(SubscriptionPayment)
admin.site.register(Discount)