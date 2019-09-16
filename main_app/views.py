from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Song
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'landing.html')

@login_required
def mymusic(request):
    song = Song.objects.all()
    return render(request, 'mymusic/collection.html',{ 'song': song })

@login_required
def playlists(request):
    song = Song.objects.all()
    return render(request, 'mymusic/playlists.html',{ 'song': song })

@login_required
def favorite_tracks(request):
    song = Song.objects.all()
    return render(request, 'mymusic/favorite_tracks.html', { 'song': song })

@login_required
def discover(request):
    song = Song.objects.all()
    return render(request, 'discover.html',{ 'song': song })

@login_required
def new(request):
    return render(request, 'mymusic/new.html')

@login_required
def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'mymusic/details.html', { 'song': song })

@login_required
def profile(request):
    song = Song.objects.all()
    return render(request, 'registration/profile.html',{ 'song': song })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration/profile.html')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
