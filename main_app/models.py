from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=1000)
    refresh_token = models.CharField(max_length=1000)
    spotify_id = models.CharField(max_length=1000) 
    spotify_display_name = models.CharField(max_length=1000)
    spotify_product = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)


class Artist(models.Model):
    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=1000)
    followers = models.IntegerField()
    image_url = models.CharField(max_length=1000)


class Album(models.Model):
    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    artist_name = models.CharField(max_length=200)
    total_tracks = models.IntegerField()
    release_date = models.CharField(max_length=200)


class Track(models.Model):
    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=1000)
    preview_url = models.CharField(max_length=1000)
    artist_name = models.CharField(max_length=200)
    duration_ms = models.IntegerField()
    track_number = models.IntegerField()
    
    
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    track = models.ForeignKey(Track,  on_delete=models.CASCADE)
