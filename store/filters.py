from .models import Product
import django_filters

class ProductSearch(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['product_name']

class ProductFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    product_address = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'product_category',
            'product_address',
            'joined_date',
            'delivery',
            'credit',
        ]
