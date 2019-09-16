import base64, json, requests
from main_app.models import Song, Profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from env import *


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