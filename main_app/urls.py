from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mymusic/', views.mymusic, name='music'),
  path('discover/', views.discover, name='discover'),
  path('mymusic/new', views.new, name='new'),
  path('mymusic/<int:song_id>/', views.song_detail, name='details'),
  path('accounts/profile', views.profile, name='profile'),
]