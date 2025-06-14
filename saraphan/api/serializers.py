from django.contrib.auth import get_user_model
from rest_framework import serializers

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


class CartGoodsWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartGoods
        fields = '__all__'
        read_only_fields = ['user']


class CartGoodsReadSerializer(serializers.ModelSerializer):
    # good = serializers.ReadOnlyField(source='good.name')
    good = GoodsSerializer()

    class Meta:
        model = CartGoods
        fields = ['good', 'amount']
