from rest_framework import routers
from . import views
from django.urls import path, include


app_name = 'content'
router = routers.DefaultRouter()

router.register(r'video_content', views.VideoContentViewSet, basename='video_content' )
router.register(r'admin', views.ContentViewSet, basename='content')

urlpatterns = [
    path("like_deslike/<slug:content>/", views.LikeDislikeView.as_view(), name="like_dislike"),
    path("", views.ContentListView.as_view(), name="content_list"),
    path('', include(router.urls)),
]