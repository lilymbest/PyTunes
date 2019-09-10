from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'base.html')

def mymusic(request):
    return render(request, 'collection.html')

def discover(request):
    return render(request, 'discover.html')

def new(request):
    return render(request, 'new.html')