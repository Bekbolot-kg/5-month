from rest_framework.test import APITestCase
from rest_framework import status
from product.models import Category, Product, Review, Color
from django.urls import reverse


class ProductViewsAPITestCase(APITestCase):
    fixtures = ['categories.json', 'products.json', 'reviews.json', 'colors.json']

    def test_get_categories(self):
        url = reverse('product:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Category.objects.count())

    def test_create_category(self):
        url = reverse('product:category-list')
        data = {'name': 'sport'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.filter(name='sport').exists(), True)

    def test_get_products(self):
        url = reverse('product:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Product.objects.count())

    def test_create_product(self):
        url = reverse('product:product-list')
        data = {
            'title': 'гантель',
            'description': '10 кг',
            'price': '1000.00',
            'category': 1,
            'colors': [1, 2]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.filter(title='гантель').exists(), True)

    def test_update_product(self):
        product = Product.objects.first()
        url = reverse('product:product-detail', args=[product.id])
        data = {
            'title': 'скакалка',
            'description': 'электронный',
            'price': '500',
            'category': product.category.id,
            'colors': [color.id for color in product.colors.all()]
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.title, 'скакалка')

    def test_delete_product(self):
        product = Product.objects.first()
        url = reverse('product:product-detail', args=[product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.filter(id=product.id).exists(), False)
