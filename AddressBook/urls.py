from django.urls import path

from . import views

app_name = 'AddressBook'
urlpatterns = [
    # ex: /addressbook/5/
    path('', views.index, name='index'),
    # ex: /contact/5/
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    # ex: /create/contact/
    path('create/contact/', views.createContact, name='createContact'),
    # ex: /delete/contact/5/
    path('delete/contact/<int:contact>/', views.deleteContact, name='list'),
    # ex: /contacts/
    path('contacts/', views.list, name='list'),
    
]