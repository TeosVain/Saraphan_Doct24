from django.db.models import Sum, F

from goods.models import CartGoods


def aggregate_goods(user):
    queryset = (
        CartGoods.objects
        .filter(user=user).select_related('good')
    )
    total_data = queryset.aggregate(
        total_amount=Sum('amount'),
        total_price=Sum(F('amount') * F('good__price'))
    )
    return total_data
