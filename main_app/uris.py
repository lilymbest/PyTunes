from django.urls import path, include
from . import spotify_views


urlpatterns = [
  path('link-user/', spotify_views.link_user, name = 'fetch-code'),
  path('receive-code/', spotify_views.handle_code),
  path('renew-token/', spotify_views.renew_token),
]