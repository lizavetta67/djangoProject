from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import Todolists
from .serializers import TodolistsModelSerializer

class TodolistModelViewSet(ModelViewSet):
    queryset = Todolists.objects.all()
    serializer_class = TodolistsModelSerializer

