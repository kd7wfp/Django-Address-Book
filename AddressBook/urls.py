from django.urls import path

from . import views

urlpatterns = [
    # ex: /addressbook/5/
    path('', views.index, name='index'),
    # ex: /contact/5/
    path('contact/<int:contact>/', views.contact, name='contact'),
    # ex: /create/contact/
    path('create/contact/', views.createContact, name='createContact'),
    # ex: /delete/contact/5/
    path('delete/contact/<int:contact>/', views.deleteContact, name='list'),
    # ex: /contacts/
    path('contacts/', views.list, name='list'),
]