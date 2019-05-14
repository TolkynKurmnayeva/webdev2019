from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    new = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    old = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ('name', 'created_at', 'due_on', 'status')
