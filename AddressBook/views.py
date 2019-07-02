from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    f = open(os.path.abspath(os.path.curdir) + '\README.md', 'r')
    file_content = f.read()
    # file_content = os.path.abspath(os.path.curdir)
    f.close()
    return HttpResponse(file_content, content_type="text/plain")