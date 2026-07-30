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
    path('',include(router.urls)),
]