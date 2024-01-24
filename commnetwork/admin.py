from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from commnetwork.models import Supplier, Product, NetworkLink


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('level', 'name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier')


class CityFilter(admin.SimpleListFilter):
    title = 'Город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = NetworkLink.objects.values_list('city', flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city=self.value())
        return queryset


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NetworkLink._meta.fields] + ['supplier_link']
    list_filter = (CityFilter,)

    def clear_debt_to_supplier(self, request, queryset):
        queryset.update(debt_to_supplier=0)
    clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"

    actions = ['clear_debt_to_supplier']

    def supplier_link(self, obj):
        url = reverse('admin:commnetwork_supplier_change', args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', url, obj.supplier)
    supplier_link.short_description = 'Ссылка на поставщика'
