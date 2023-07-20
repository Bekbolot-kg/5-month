from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='product')
router.register(r'product', ProductViewSet, basename='category')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'colors', ReviewViewSet, basename='colors')


app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
]
