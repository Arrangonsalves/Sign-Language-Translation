from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("SigntoText", views.SigntoText, name='SigntoText'),
    path("TexttoSign", views.TexttoSign, name='TexttoSign'),
    path("AboutUs", views.AboutUs, name='AboutUs'),
    path("Contact", views.Contact, name='Contact'),
    path("details",views.details,name='details')

    
]
