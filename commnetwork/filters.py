import django_filters
from commnetwork.models import Supplier


class SupplierFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = ('country',)
