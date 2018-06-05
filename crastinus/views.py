from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(return'index.html')
