from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def harika(request,name):
    return HttpResponse(f'Welcome to File {name}')