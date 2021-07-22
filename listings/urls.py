from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings,name="listings"),
    path('listings/', views.listing,name="listing")
    
   
]