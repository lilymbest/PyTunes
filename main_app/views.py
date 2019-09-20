from django.shortcuts import render, redirect
from main_app.models import Profile, Track, Playlist, Artist
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests, json

class PlaylistCreate(CreateView):
    model = Playlist
    fields = ['name', 'description']
    success_url = '/accounts/profile'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        print(form)
        return super().form_valid(form)

class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = '/accounts/profile'

class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = ['name', 'description']
    success_url = '/accounts/profile'
    
# Create your views here.
def base(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'base.html',{ 'profile': profile })

def home(request):
    return render(request, 'landing.html')

@login_required
def playlist_details(request, playlist_id):
    profile = Profile.objects.get(user=request.user)
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'main_app/playlist_detail.html', {'playlist': playlist, 'profile': profile})

@login_required
def discover(request):
    playlists = Playlist.objects.all()
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        access_token = profile.access_token
        body = request.POST
        search_type = body['type']
        header = {
            "Authorization": f"Bearer {access_token}"
        }
        payload = {
            "q": body['query'],
            "type": search_type,        
        }
        results = requests.get('https://api.spotify.com/v1/search', params=payload, headers=header)
        results = json.loads(results.text)
        print(results)
        if search_type == 'artist':
            results = results['artists']
        if search_type == 'album':
            results = results['albums']
        if search_type == 'track':
            results = results['tracks']
        if search_type == 'playlist':
            results = results['playlists']
        return render(request, 'discover.html',{'results': results, "profile": profile, 'type': search_type, 'playlists': playlists })
    else:
        return redirect('home')


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    playlists = Playlist.objects.filter(profile=profile)
    return render(request, 'registration/profile.html', { 'profile': profile, 'playlists': playlists })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fetch-code')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


