from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

# Create your views here.
def index2(request):
    return render( request, 'index2.html')

def girl(request):
    return render( request, 'girl.html')

def girl2(request):
    return render( request, 'girl2.html')

def train(request):
    return render( request, 'train.html')


def help(request):
    return render( request, 'help.html')
