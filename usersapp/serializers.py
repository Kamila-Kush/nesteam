from django.contrib.auth.models import User
from rest_framework import serializers
from usersapp.models import Player


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "id", "username", "contacts", "first_name"]

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'