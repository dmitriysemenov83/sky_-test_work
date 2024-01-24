from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from commnetwork.filters import SupplierFilter
from commnetwork.models import Supplier, Product, NetworkLink
from commnetwork.paginators import SupplierPaginator, ProductPaginator, NetworkLinkPaginator
from commnetwork.serializers import SupplierSerializer, ProductSerializer, NetworkLinkSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all().order_by('-id')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SupplierFilter
    pagination_class = SupplierPaginator
    permission_classes = [IsAuthenticated]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator
    permission_classes = [IsAuthenticated]


class NetworkLinkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    pagination_class = NetworkLinkPaginator
    permission_classes = [IsAuthenticated]

