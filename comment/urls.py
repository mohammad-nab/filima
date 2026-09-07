from django.urls import path
from . import views


app_name = 'comment'
urlpatterns = [
    path('send_comment/<slug:content>/', views.SendCommentView.as_view(), name='send_comment'),
    path('get_comment/<slug:content>/', views.GetCommentView.as_view(), name='get_comment'),
    path('list_comment/', views.AdminListCommentView.as_view(), name='list_comment'),
    path('approve_comment/<uuid:comment_uuid>/', views.AdminApproveCommentView.as_view(), name='approve_comment'),

]