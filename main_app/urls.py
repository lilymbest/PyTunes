from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mymusic/', views.mymusic, name='music'),
  path('discover/', views.discover, name='discover'),
  path('mymusic/new', views.new, name='new'),
  path('mymusic/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
  path('mymusic/favorite_tracks/<track_id>/', views.favorite_tracks, name="favorite_tracks"),
  path('mymusic/favorite_tracks', views.favorite_tracks, name="favorite_tracks"),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
]

