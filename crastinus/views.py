from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

# Create your views here.
def index2(request):
    return render( request, 'index2.html')


def help(request):
    return render( request, 'help.html')
