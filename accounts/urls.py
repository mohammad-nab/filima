from django.urls import path, include
from . import views
from rest_framework import routers




router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('check_otp/', views.CheckOTPCodeView.as_view(), name='check_otp'),
    path("auth/me/", views.UserRetrieveUpdateAPIView.as_view(), name="auth-me"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path(
        "upload_profile_pic/",
        views.UserUploadProfilePicView.as_view(),
        name="upload_profile_pic"
    ),
    path('', include(router.urls)),
]
