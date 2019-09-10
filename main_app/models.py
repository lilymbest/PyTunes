from django.db import models

# Create your models here.
class Song(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.TextField(max_length=250)
    rating = models.IntegerField()
    def __str__(self):
        return self.name