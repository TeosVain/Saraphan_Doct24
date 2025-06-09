from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from goods.models import Category, Goods, Subcategory, CartGoods
from api.serializers import CategorySerializer, GoodsSerializer, CartGoodsSerializer
from users.models import User


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodsListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CartGoodsViewSet(viewsets.ModelViewSet):
    serializer_class = CartGoodsSerializer
    queryset = CartGoods.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartGoods.objects.filter(user=User.objects.get(id=1))

    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(id=1))
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
