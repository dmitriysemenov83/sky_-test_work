from rest_framework import serializers
from commnetwork.models import Supplier, Product, NetworkLink


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkLink
        fields = '__all__'

    def update(self, instance, validated_data):
        # Исключаем поле "Задолженность перед поставщиком" из обновляемых полей
        if 'debt_to_supplier' in validated_data:
            raise serializers.ValidationError("Нельзя обновить поле 'Задолженность перед поставщиком'")
        return super().update(instance, validated_data)
