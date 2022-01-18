# from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from rest_framework import permissions
from rest_framework import serializers
from .serializers import MovieSerializer
from .models import Movie

from djangocrud.api.serializers import MovieSerializer


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    # permission_classes = [permissions.IsAuthenticated]

