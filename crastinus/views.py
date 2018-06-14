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
from allauth.socialaccount.models import SocialToken

# Create your views here.
@login_required
def home(request):
    ruid = request.user.id
    user = get_object_or_404(User, id=ruid)
    allproviders = user.socialaccount_set.all()
    # print(allproviders[0].__dict__)
    usedproviders = [a.provider for a in allproviders]
    providers = [a.capitalize() for a in usedproviders]
    if 'Linkedin_oauth2' in providers:
        linkindex = providers.index('Linkedin_oauth2')
        providers[linkindex] = 'Linkedin'
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


    if 'Linkedin' in providers:
        print('Linkedin registered')
        print('displaying...')
        Linkedin = True
        # faceuid = allproviders[usedproviders.index('facebook')].uid
        # facetokenraw = SocialToken.objects.filter(account__user=user, account__provider='facebook')
        # facetoken = facetokenraw.first()
        # facedata = requests.get("https://graph.facebook.com/{}/feed?access_token={}".format(faceuid, facetoken)).json()
        linktokenraw = SocialToken.objects.filter(account__user=user, account__provider='linkedin_oauth2').first().token
        # linkdata = requests.get('https://api.linkedin.com/v2/activityFeeds?q=networkShares&count=2', headers={'Authorization':linktokenraw}).json()
        # linkdata = requests.get('https://api.linkedin.com/v2/activityFeeds?q=networkShares&count=2', auth=linktokenraw).json()
        linkdata = requests.get('https://api.linkedin.com/v1/people/~?format=json', headers={'Authorization':'Bearer ' + linktokenraw}).json()




    else:
        print('Linkedin registration failed')
        print('cannot be displayed')
        Linkedin = False
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
    # print(allproviders[0].uid)
    return render(request, 'home.html', {'twitter' : Twitter, 'followernum' : followernum, 'notifications' : notifications, 'linkdata' : linkdata})

def user_logout(request):
    logout(request)
    return redirect('Home')