from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact
import os


# Create your views here.

def index(request):
    f = open(os.path.abspath(os.path.curdir) + '\README.md', 'r')
    file_content = f.read()
    file_content = os.path.abspath(os.path.curdir)
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

def contact(request, contact):
    return HttpResponse("You're looking at contact %s." % contact)

def createContact(request):
    return HttpResponse("You're looking at createContact")

def deleteContact(request, contact):
    return HttpResponse("You're looking at deleteContact")

def list(request):
    contact_list = Contact.objects.order_by('last_name')[:5]
    template = loader.get_template('AddressBook/index.html')
    context = {
        'contact_list': contact_list,
    }
    return HttpResponse(template.render(context, request))

def searchAndFilter(request, contact):
    return HttpResponse("You're looking at searchAndFilter")
