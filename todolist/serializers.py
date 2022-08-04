from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Todolists

class TodolistsModelSerializer(ModelSerializer):
    class Meta:
        model = Todolists
        fields = '__all__'