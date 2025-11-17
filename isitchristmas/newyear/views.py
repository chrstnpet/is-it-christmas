from django.shortcuts import render
from django.http import HttpResponse

def newyear(request):
    return HttpResponse("Hello World!")