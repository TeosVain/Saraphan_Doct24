from rest_framework.pagination import PageNumberPagination

from saraphan.constants import DEFAULT_PAGINATOR_LIMIT


class CustomPageNumberPaginator(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = DEFAULT_PAGINATOR_LIMIT
