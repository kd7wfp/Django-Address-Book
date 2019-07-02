from django.shortcuts import render, redirect
from django.http import HttpResponse
from AddressBook import views

# Create your views here.
def navToAddressBook(request):
    return redirect('/admin/login')