from rest_framework import routers
from . import views


app_name = 'content'
router = routers.DefaultRouter()
router.register('', views.ContentViewSet, basename='content')

urlpatterns = router.urls