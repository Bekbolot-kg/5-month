from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'colors', 'get_rating', 'get_category_name', 'category',
                  'created_at']

    def create(self, validated_data):
        colors_data = validated_data.pop('colors')
        product = Product.objects.create(**validated_data)

        for color_data in colors_data:
            Color.objects.create(product=product, **color_data)

        return product

    def update(self, instance, validated_data):
        colors_data = validated_data.pop('colors')
        colors = instance.colors.all()
        colors = list(colors)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        for color_data in colors_data:
            color = colors.pop(0)
            color.name = color_data.get('name', color.name)
            color.save()

        return instance


