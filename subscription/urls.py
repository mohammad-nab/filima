from django.urls import path
from rest_framework import routers
from subscription.views import SubscriptionViewSet, DiscountViewSet, CreateRandomDiscountCodeView

app_name = 'subscription'
router = routers.DefaultRouter()
router.register(r'', SubscriptionViewSet, basename='subscription')
router.register(r'discount', DiscountViewSet, basename='discount')

urlpatterns = [
    path('discount/create_random_discount_code/', CreateRandomDiscountCodeView.as_view(), name='create_random_discount_code'),
]
urlpatterns += router.urls