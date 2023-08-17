from django_filters import rest_framework as filters
import django_filters
from .models import Player

class PlayerFilter(filters.FilterSet):
    nick_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Player
        fields = ['nick_name']