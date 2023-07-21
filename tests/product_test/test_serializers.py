from rest_framework.test import APITestCase
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer, ColorSerializer

class SerializerTestCase(APITestCase):
    fixtures = ['categories.json', 'products.json', 'reviews.json', 'colors.json']

    def test_category_serializer(self):
        category = Category.objects.first()
        serializer = CategorySerializer(instance=category)
        expected_data = {'id': category.id, 'name': category.name, 'products_count': category.products_count}
        self.assertEqual(serializer.data, expected_data)

    def test_product_serializer(self):
        product = Product.objects.first()
        serializer = ProductSerializer(instance=product)
        expected_data = {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': str(product.price),
            'get_rating': product.get_rating,
            'get_category_name': product.get_category_name(),
            'category': product.category_id,
            'created_at': product.created_at,
            'colors': ColorSerializer(product.colors.all(), many=True).data
        }
        self.assertEqual(serializer.data, expected_data)
