from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Song
# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'landing.html',{ 'songs': songs })

def mymusic(request):
    songs = Song.objects.all()
    return render(request, 'mymusic/collection.html',{ 'songs': songs })

def discover(request):
    songs = Song.objects.all()
    return render(request, 'discover.html',{ 'songs': songs })

def new(request):
    return render(request, 'mymusic/new.html')

# def song_detail(request, song_id):
#     song = Song.objects.get(id=song_id)
#     return render(request, 'mymusic/details.html')