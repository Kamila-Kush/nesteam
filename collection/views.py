from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import GameCollection
from .serializers import CollectionSerializer
from .filters import CollectionFilter

class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = CollectionFilter



