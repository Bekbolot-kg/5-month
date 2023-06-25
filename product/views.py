from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(category)
    return JsonResponse(serializer.data)


def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)


def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)


def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return JsonResponse(serializer.data)
