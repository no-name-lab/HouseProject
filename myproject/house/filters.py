from django_filters.rest_framework import FilterSet
from .models import *


class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'transaction_type': ['exact'],
            'title': ['exact'],
            'property_type': ['exact'],
            'region': ['exact'],
            'condition_type': ['exact'],
            'city': ['exact'],
            'district': ['exact'],
            'area': ['gt', 'lt'],
            'price': ['gt', 'lt'],
            'floor': ['gt', 'lt'],
            'total_floors': ['exact']
        }