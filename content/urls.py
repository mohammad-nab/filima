from rest_framework import routers
from . import views
from django.urls import path, include


app_name = 'content'
router = routers.DefaultRouter()
router.register('', views.ContentViewSet, basename='content')

urlpatterns = [
    path("like_deslike/<slug:content>/", views.LikeDislikeView.as_view(), name="like_dislike"),
    path('', include(router.urls)),
]