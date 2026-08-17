from rest_framework import routers
from image.views import ImageViewSet


app_name = 'image'
router = routers.DefaultRouter()
router.register('', ImageViewSet, basename='image')

urlpatterns = []
urlpatterns += router.urls