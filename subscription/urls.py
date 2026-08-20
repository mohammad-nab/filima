from rest_framework import routers
from subscription.views import SubscriptionViewSet


app_name = 'subscription'
router = routers.DefaultRouter()
router.register(r'', SubscriptionViewSet, basename='subscription')

urlpatterns = []
urlpatterns += router.urls