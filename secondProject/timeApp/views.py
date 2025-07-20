from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def telltime(request):
    time = datetime.datetime.now()
    return HttpResponse('<h1>The Time is: ' + str(time) + '</h1>')