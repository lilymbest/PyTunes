from django.urls import path, include
from . import spotify_views


urlpatterns = [
  path('link-user/', spotify_views.link_user, name = 'fetch-code'),
  path('receive-code/', spotify_views.handle_code),
  # path('spotify/receive-token/', spotify-views.handle_token),
]