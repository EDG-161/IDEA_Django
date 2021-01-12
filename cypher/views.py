from django.http import HttpResponse
from . import logic
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Home")
