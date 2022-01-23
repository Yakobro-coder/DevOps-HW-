from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductFilter(filters.FilterSet):
    products = filters.CharFilter(field_name='products__description', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = []


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    search_fields = ['description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    filterset_fields = ['products']
    filterset_class = ProductFilter
