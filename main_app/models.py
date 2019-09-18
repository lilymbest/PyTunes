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

class Song(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.TextField(max_length=250)
    rating = models.IntegerField()
    def __str__(self):
        return self.name