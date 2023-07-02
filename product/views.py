from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True)
    return Response(data=data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    data = CategorySerializer(category)
    return Response(data=data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True)
    return Response(data=data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    data = ProductSerializer(product)
    return Response(data=data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True)
    return Response(data=data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    data = ReviewSerializer(review)
    return Response(data=data.data, status=status.HTTP_200_OK)
