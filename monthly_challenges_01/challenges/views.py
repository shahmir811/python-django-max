from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse('This world is full of challenges. But we are here to face them all. Let us start with the first one. The first challenge is to create a Django project and run it on the server. Let us see if you can do it. Good luck!')

def february(request):
    return HttpResponse('This is the challenge for February. The challenge is to create a Django app and run it on the server. Let us see if you can do it. Good luck!')