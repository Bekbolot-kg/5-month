import random

from rest_framework import serializers
from .models import CustomUser

class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8)

    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).count() > 0:
            raise serializers.ValidationError('Такой логин уже существует')
        return username

    def create(self, validated_data):
        random_code = ''.join(str(random.randint(0, 9)) for _ in range(6))
        validated_data['confirmation_code'] = random_code
        return CustomUser.objects.create(**validated_data)
