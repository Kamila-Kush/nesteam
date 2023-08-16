from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *


from .serializers import UserListSerializer
def users_list(request):
    users_lst = User.objects.all()
    serializer = UserListSerializer(users_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def user_detail(request, pk):
    user_object = User.objects.get(pk=pk)
    serializer = UserListSerializer(user_object)
    return JsonResponse(serializer.data, safe=False)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer