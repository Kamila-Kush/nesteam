from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse


from .serializers import UserSerializer
def users_list(request):
    users_lst = User.objects.all()
    serializer = UserSerializer(users_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)
