from django.urls import include, path
from rest_framework import routers

from api.views import CategoryListView, GoodsListView, CartGoodsViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('cart', CartGoodsViewSet, basename='cartgoods')

v1_patterns = [
    path('', include(router_v1.urls)),
    path('goods/', GoodsListView.as_view(), name='goods-list'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('', include('djoser.urls')),
]

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(v1_patterns)),
]
