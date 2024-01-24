from django.db import models
from users.models import NULLABLE


class Supplier(models.Model):
    LEVEL_CHOICES = (
        ('Factory', 'Завод'),
        ('Retail Network', 'Розничная сеть'),
        ('Individual Entrepreneur', 'ИП'),
    )

    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, verbose_name='поставщик')
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='эл.почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=255, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода на рынок')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkLink(models.Model):
    ORGANIZATION_CHOICES = (
        ('Retail Network', 'Розничная сеть'),
        ('Individual Entrepreneur', 'ИП'),
    )
    organization = models.CharField(max_length=50, choices=ORGANIZATION_CHOICES, verbose_name='организация')
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='эл.почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='задолженность')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)

    class Meta:
        verbose_name = 'Сетевая связь'
        verbose_name_plural = 'Сетевые связи'
