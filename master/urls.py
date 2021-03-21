from csd_org import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact_req/', views.contact_request, name='contact_post'),
    path('subscribe_req/', views.subscribe_request, name='subscribe_post'),
]
