from django.urls import path

from . import views

urlpatterns = [
    # ex: /addressbook/5/
    path('', views.index, name='index'),
    # ex: /addressbook/5/
    path('login/', views.login, name='login'),
    # ex: /addressbook/5/
    path('logout/', views.logout, name='logout'),
]