from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import twitter
twitterapi = twitter.Api()
import requests
from crastinus.apis import twitterapi
import time
import requests
import json

# Create your views here.
# def index(request):
#     return render(request, 'home.html')

# TWITTER
# def home(request):
#     followers = twitterapi.GetFollowers()
#     print([f.name for f in followers])
#     followernum = len(followers)
#     statuses = twitterapi.GetHomeTimeline()
#     print(statuses)
    
#     for status in statuses:
#         age = int(time.time()) - status.created_at_in_seconds
#         if age < 60:
#             status.age = str(int(age)) + ' seconds ago'
#         if age == 1:
#             status.age = '1 second ago'
#         if 60 < age < 3600:
#             minutes = age/60
#             status.age = str(int(minutes)) + ' minutes ago'
#         if 59 < age < 119:
#             status.age = '1 minute ago'
#         if 3600 < age < 86400:
#             hours = age/3600
#             status.age = str(int(hours)) + ' hours ago'
#         if 3600 < age < 7199:
#             status.age = '1 hour ago'
#         if 86400 < age < 2592000:
#             days = age/86400
#             status.age = str(int(days)) + ' days ago'
#         if 86400 < age < 172799:
#             status.age = '1 day ago'
#         if 2592000 < age < 31104000:
#             months = age/2592000
#             status.age = str(int(months)) + ' months ago'
#         if 2592000 < age < 5183999:
#             status.age = '1 month ago'
#         if age > 31104000:
#             years = age/31104000
#             status.age = str(int(years)) + ' years ago'
#         if 31104000 < age < 62207999:
#             status.age = '1 year ago'

#     print([s.age for s in statuses])
#     return render(request, 'home.html', {'followernum' : followernum, 'statuses' : statuses})

# INSTAGRAM
# def home(request):
#     r = requests.get("https://api.instagram.com/v1/users/self/feed?access_token=5946843692.64916c7.ba9973b5120941edb2e4c9a853d33f27&count=10").json()
#     print (r)
#     return render(request, 'home.html')



@login_required
def home(request):
    ruid = request.user.id
    user = get_object_or_404(User, id=ruid)
    # r = requests.get("https://graph.facebook.com/820882001277849/feed").json()
    # print (r)
    allproviders = user.socialaccount_set.all()
    usedproviders = [a.provider for a in allproviders]
    providers = [a.capitalize() for a in usedproviders]
    print(providers)
    notifications = []
    # DEFINING TWITTER VARIABLE
    followernum = 0
    facedata = 0

    if 'Twitter' in providers:
        print('Twitter registered')
        print('displaying...')
        Twitter = True
        # TWITTER LOGIC
        followers = twitterapi.GetFollowers()
        didi = followers[0]
        print([f.name for f in followers])
        followernum = len(followers)
        statuses = twitterapi.GetHomeTimeline()
        for status in statuses:
            status.provider = twitter
            status.poster = status.user.screen_name
            status.rage = status.created_at_in_seconds
        dudu = statuses[0]
        print(statuses)
        notifications.extend(statuses)
        
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

    else:
        print('Twitter registration failed')
        Twitter = False


    if 'Instagram' in providers:
        print('Instagram registered')
        print('displaying...')
        Instagram = True
    else:
        print('Instagram registration failed')
        Instagram = False


    if 'Facebook' in providers:
        print('Facebook registered')
        print('displaying...')
        Facebook = True
        faceuid = allproviders[usedproviders.index('facebook')].uid
        faceresponse = requests.get("https://graph.facebook.com/{}/feed".format(faceuid)).json()
        facedata = json.loads(faceresponse.text)

    else:
        print('Facebook registration failed')
        print('cannot be displayed')
        Facebook = False
        # FACEBOOK LOGIC

    notifications.sort(key=lambda x: x.rage, reverse=True)
    print('notifications:')
    print(notifications)
    # print(didi.__dict__)
    # print(didi.followers_count) #TWITTER FOLLOWERS COUNT
    # print(didi.screen_name) #TWITTER SCREEN NAME
    # print(didi.friends_count) #TWITTER FOLLOWING COUNT
    # print(dudu.__dict__)
    # print (objjj.__dict__)
    print(allproviders[0].uid)
    return render(request, 'home.html', {'twitter' : Twitter, 'instagram' : Instagram, 'facebook' : Facebook, 'followernum' : followernum, 'notifications' : notifications, 'facedata' : facedata})

def user_logout(request):
    logout(request)
    return redirect('Home')