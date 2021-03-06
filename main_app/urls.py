from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('discover/', views.discover, name='discover'),
  path('mymusic/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
  path('mymusic/playlist/<int:pk>/', views.PlaylistDelete.as_view(), name='playlist_delete'),
  path('mymusic/playlist/<int:pk>/update', views.PlaylistUpdate.as_view(), name='playlist_update'),
  path('mymusic/<int:playlist_id>/', views.playlist_details, name="playlist_details"),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
]
