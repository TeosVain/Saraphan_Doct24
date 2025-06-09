from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from saraphan import constants, fields
from goods.models import Category, Goods, Subcategory, CartGoods

User = get_user_model()


class CategorySubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug', 'image',]
        model = Subcategory


class CategorySerializer(serializers.ModelSerializer):
    subcategories = CategorySubcategorySerializer(
        many=True, required=True
    )

    class Meta:
        fields = ['name', 'slug', 'image', 'subcategories',]
        model = Category


class GoodsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Goods
        fields = (
            'name', 'slug', 'text', 'price', 'subcategory', 'images',
        )

    def get_images(self, obj):
        request = self.context.get('request')
        return [
            request.build_absolute_uri(obj.image_thumbnail.url),
            request.build_absolute_uri(obj.image_medium.url),
            request.build_absolute_uri(obj.image_large.url)
        ]


class CartGoodsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    good = serializers.ReadOnlyField(source='good.name')

    class Meta:
        model = CartGoods
        fields = '__all__'
