from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You're looking at users index")

def login(request):
    return HttpResponse("You're looking at login")

def logout(request):
    return HttpResponse("You're looking at logout")