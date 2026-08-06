from rest_framework import routers
from . import views


app_name = 'tags'
router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'actor', views.ActorViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'language_status', views.LanguageStatusViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'banner_location', views.BannerLocationViewSet)
router.register(r'target_audience', views.TargetAudienceViewSet)
router.register(r'inform_type', views.InformTypeViewSet)
router.register(r'account_status', views.AccountStatusViewSet)


urlpatterns = []
urlpatterns += router.urls
