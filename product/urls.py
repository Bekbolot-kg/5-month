from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'colors', ReviewViewSet, basename='colors')

app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
]
