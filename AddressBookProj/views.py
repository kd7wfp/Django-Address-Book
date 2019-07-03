from django.shortcuts import render, redirect
from django.http import HttpResponse
from AddressBook import views

# Create your views here.
def navToAddressBookLogin(request):
    return redirect('/AddressBookUsers/login')