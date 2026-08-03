from rest_framework import routers
from . import views


app_name = 'tags'
router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)


urlpatterns = []
urlpatterns += router.urls