from django.urls import path

from .views import category_list, category_detail, product_list, product_detail, review_list, review_detail

app_name = 'product'

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:id>/', category_detail, name='category-detail'),
    path('products/', product_list, name='product-list'),
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:id>/', review_detail, name='review-detail'),
]
