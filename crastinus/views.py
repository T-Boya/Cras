from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import twitter
twitterapi = twitter.Api()
import requests
from crastinus.apis import twitterapi
import time

# Create your views here.
# def index(request):
#     return render(request, 'home.html')

def home(request):
    followers = twitterapi.GetFollowers()
    print([f.name for f in followers])
    followernum = len(followers)
    statuses = twitterapi.GetHomeTimeline()
    print(statuses)
    for status in statuses:
        age = int(time.time()) - status.created_at_in_seconds
        if age < 60:
            status.age = str(int(age)) + ' seconds ago'
        if age == 1:
            status.age = '1 second ago'
        if 60 < age < 3600:
            minutes = age/60
            status.age = str(int(minutes)) + ' minutes ago'
        if 59 < age < 119:
            status.age = '1 minute ago'
        if 3600 < age < 86400:
            hours = age/3600
            status.age = str(int(hours)) + ' hours ago'
        if 3600 < age < 7199:
            status.age = '1 hour ago'
        if 86400 < age < 2592000:
            days = age/86400
            status.age = str(int(days)) + ' days ago'
        if 86400 < age < 172799:
            status.age = '1 day ago'
        if 2592000 < age < 31104000:
            months = age/2592000
            status.age = str(int(months)) + ' months ago'
        if 2592000 < age < 5183999:
            status.age = '1 month ago'
        if age > 31104000:
            years = age/31104000
            status.age = str(int(years)) + ' years ago'
        if 31104000 < age < 62207999:
            status.age = '1 year ago'

    print([s.age for s in statuses])
    return render(request, 'home.html', {'followernum' : followernum, 'statuses' : statuses})


def user_logout(request):
    logout(request)
    return redirect('Home')