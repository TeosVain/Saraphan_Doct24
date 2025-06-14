from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.permissions import IsCartOwner
from api.serializers import (
    CategorySerializer,
    GoodsSerializer,
    CartGoodsWriteSerializer,
    CartGoodsReadSerializer
)
from api.utiles import aggregate_goods
from goods.models import Category, Goods, CartGoods


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class GoodsListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [AllowAny]


class CartGoodsViewSet(viewsets.ModelViewSet):
    read_serializer_class = CartGoodsReadSerializer
    write_serializer_class = CartGoodsWriteSerializer
    pagination_class = None
    permission_classes = [IsCartOwner, IsAuthenticated]

    def get_queryset(self):
        return CartGoods.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return self.write_serializer_class
        return self.read_serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        total_data = aggregate_goods(request.user)
        response.data = {
            'results': response.data,
            'total_amount': total_data['total_amount'] or 0,
            'total_price': total_data['total_price'] or 0
        }
        return response

    @action(detail=False, methods=['get'], url_path='clear_cart')
    def clear_cart(self, request):
        CartGoods.objects.filter(user=request.user).delete()
        return Response(
            {'message': 'Cart cleared successfully.'},
            status=status.HTTP_200_OK
        )
