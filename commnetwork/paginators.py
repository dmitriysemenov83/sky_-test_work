from rest_framework.pagination import PageNumberPagination


class SupplierPaginator(PageNumberPagination):
    page_size = 5


class ProductPaginator(PageNumberPagination):
    page_size = 5


class NetworkLinkPaginator(PageNumberPagination):
    page_size = 5

