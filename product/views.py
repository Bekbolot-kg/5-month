from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *


class ProductPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()
    price = filters.NumberFilter(lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['created_at', 'price']

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('colors')
        return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
