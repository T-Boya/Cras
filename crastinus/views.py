from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse('It Works!')

@login_required
def home(request):
    return render(request, 'home.html')