from django_filters import rest_framework as filters
import django_filters
from .models import GameCollection

class CollectionFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    games_list__gt = filters.NumberFilter(field_name='games_list', lookup_expr='gte')
    games_list__lt = filters.NumberFilter(field_name='games_list', lookup_expr='lte')
    class Meta:
        model = GameCollection
        fields = ['name', 'games_list']
