from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('myprofile', views.profile, name='myprofile'),
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('photo/<int:photo_id>/', views.view_photo, name='view_photo'),
    path('video/<int:video_id>/', views.view_video, name='view_video'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('video/<int:video_id>/delete/', views.delete_video, name='delete_video'),
]
