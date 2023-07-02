from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'get_rating', 'get_category_name', 'reviews']


class ProductCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    category = serializers.CharField(required=False)

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = Category.objects.get(name=category_name)
        product = Product.objects.create(category=category, **validated_data)
        return product

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.category_id = validated_data.get('category', instance.category_id)
        instance.save()
        return instance

class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False)
    stars = serializers.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')), required=False)

    def create(self, validated_data):
        product = validated_data.pop('product', None)
        review = Review.objects.create(product=product, **validated_data)
        return review

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.product = validated_data.get('product', instance.product)
        instance.save()
        return instance
