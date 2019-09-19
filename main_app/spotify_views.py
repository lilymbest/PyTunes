import base64, json, requests, os
from main_app.models import Profile, Playlist, Track
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
SPOTIFY_REDIRECT_URI_ENCODED = 'https%3A%2F%2Fpy-tunes.herokuapp.com%2Fspotify%2Freceive-code%2F'
SPOTIFY_REDIRECT_URI = 'https://py-tunes.herokuapp.com/spotify/receive-code/'


def renew_token(request):
  profile = Profile.objects.get(user=request.user)
  renew_url = 'https://accounts.spotify.com/api/token'
  body = {
    'grant_type': 'refresh_token',
    'refresh_token': profile.refresh_token,
    "client_id": SPOTIFY_CLIENT_ID,
    "client_secret": SPOTIFY_CLIENT_SECRET
  }
  r = requests.post(renew_url, data=body)
  r = json.loads(r.text)
  profile.access_token = r['access_token']
  profile.save()
  return redirect('profile')


def link_user(request):
  scope = 'user-read-private+user-read-email'
  redirect_url = SPOTIFY_REDIRECT_URI_ENCODED
  URL = f'https://accounts.spotify.com/authorize?response_type=code&client_id={SPOTIFY_CLIENT_ID}&scope={scope}&redirect_uri={redirect_url}&show_dialog=true'
  return redirect(URL)


def handle_code(request):
  code = request.META['QUERY_STRING'][5:] 
  token_url = 'https://accounts.spotify.com/api/token'
  body = { 
    "grant_type": "authorization_code",
    "code": str(code),
    "redirect_uri": SPOTIFY_REDIRECT_URI,
    "client_id": SPOTIFY_CLIENT_ID,
    "client_secret": SPOTIFY_CLIENT_SECRET
  }
  # requests access token and refresh token from Spotify 
  r = requests.post(token_url, data=body)
  r = json.loads(r.text)
  print(r)
  header = {
    "Authorization": f"Bearer {r['access_token']}"
  }
  spotify_user_info = requests.get('https://api.spotify.com/v1/me', headers=header)
  spotify_user_info = json.loads(spotify_user_info.text)
  createProfile(r, spotify_user_info, request.user)
  return redirect('profile')


def createProfile(token_responce, user_info, user):
  if len(user_info['images']) > 0:
    image = user_info['images'][0]['url']
  else:
    image = 'static/images/pytuneswhite.png'
  profile = Profile(
    user = user,
    access_token = token_responce['access_token'],
    refresh_token = token_responce['refresh_token'],
    spotify_id = user_info['id'],
    spotify_display_name = user_info['display_name'],
    spotify_product = user_info['product'],
    image_url = image
  )
  profile.save()
  return profile




def save_track(request):
  body = request.POST
  track_id = body['track_id']
  playlist_id = body['playlist_id']
  profile = Profile.objects.get(user = request.user)
  access_token = profile.access_token
  url = f"https://api.spotify.com/v1/tracks/{track_id}"
  header ={
    "Authorization": f"Bearer {access_token}"
  }
  results = requests.get(url, headers=header)
  results = json.loads(results.text)
  track = createTrack(results)
  Playlist.objects.get(id=playlist_id).tracks.add(track)
  return redirect('profile')



def createTrack(data):    
  track = Track(
    name = data['name'],
    spotify_id = data['id'],
    preview_url = data['preview_url'],
    artist_name = data['artists'][0]['name'],
    duration_ms = data['duration_ms'],
    track_number = data['track_number'],
  )
  track.save()
  return track
