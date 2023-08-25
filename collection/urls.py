from django.urls import path, include, re_path
from rest_framework import routers
from .views import *

collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionViewSet)

urlpatterns = [
    path('', include(collection_router.urls)),
    path('user-collection/', UserCollectionAPIView().as_view(), name='user-collection'),

]
