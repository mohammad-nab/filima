from django.urls import path
from . import views


app_name = 'comment'
urlpatterns = [
    path('send_comment/<slug:content>/', views.SendCommentView.as_view(), name='send_comment'),
]