from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet, ColorViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

color_router = routers.SimpleRouter()
color_router.register(r'product/<int:product_pk>/colors', ColorViewSet, basename='product-colors')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(color_router.urls)),
]
