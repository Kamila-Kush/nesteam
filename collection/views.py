from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GameCollection
from .serializers import CollectionSerializer
from .filters import CollectionFilter
from .mixins import IsCollectionAuthorMixin

class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = CollectionFilter

class UserCollectionAPIView(IsCollectionAuthorMixin, APIView):
    def get(self, request):
        collection_list = GameCollection.objects.filter(author=request.user)
        serializer = CollectionSerializer(
            instance=collection_list,
            many=True
        )
        return Response(serializer.data)

