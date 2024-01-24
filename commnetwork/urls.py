from django.urls import path

from commnetwork.apps import CommnetworkConfig
from rest_framework.routers import DefaultRouter
from commnetwork.views import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, \
    SupplierUpdateAPIView, SupplierDestroyAPIView, ProductViewSet, NetworkLinkViewSet

app_name = CommnetworkConfig.name

pr_router = DefaultRouter()
pr_router.register(r'product', ProductViewSet, basename='product')

nl_router = DefaultRouter()
nl_router.register(r'network', NetworkLinkViewSet, basename='network')

urlpatterns = [
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier-create'),
    path('supplier/list/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('supplier/retrieve/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier-retrieve'),
    path('supplier/update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier-update'),
    path('supplier/delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier-delete'),
] + pr_router.urls + nl_router.urls
