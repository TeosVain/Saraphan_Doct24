from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers

from api.views import (
    CategoryListView, GoodsListView, CartGoodsViewSet
)

router_v1 = routers.DefaultRouter()
router_v1.register('cart', CartGoodsViewSet)

user_urlpatterns = [
]

v1_patterns = [
    path('', include(router_v1.urls)),
    path('category/', CategoryListView.as_view()),
    path('goods/', GoodsListView.as_view()),
    path('', include(user_urlpatterns)),
]

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(v1_patterns)),
]