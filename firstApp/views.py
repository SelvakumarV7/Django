from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish(request):
    message = '<h1>Welcome</h1>'
    return HttpResponse(message)