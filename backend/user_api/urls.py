from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from django.urls import path


urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
   
]
