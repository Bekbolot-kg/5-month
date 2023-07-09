from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('api/v1/category_model/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/v1/category_model/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('api/v1/product_model/', ProductListAPIView.as_view(), name='product-list'),
    path('api/v1/product_model/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/v1/review_model/', ReviewListAPIView.as_view(), name='review-list'),
    path('api/v1/review_model/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
