from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=100, verbose_name='название'),
    contacts = models.ForeignKey
    products = models.ForeignKey
    provider = models.ForeignKey
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность поставщику')
    creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')


from django.db import models


class Supplier(models.Model):
    LEVEL_CHOICES = (
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur'),
    )

    level = models.IntegerField(choices=LEVEL_CHOICES)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class NetworkLink(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    products = models.ManyToManyField(Product)

    def str(self):
        return self.name

#------------------------------------------------------------------------------------------------

from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Wholesaler(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')
    products = models.ManyToManyField('Product', related_name='wholesalers')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Retailer(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')
    products = models.ManyToManyField('Product', related_name='retailers')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    # supplier = models.ForeignKey('self', on_delete=models.CASCADE, related_name='products')
    supplier = models.ForeignKey('Factory', on_delete=models.CASCADE, related_name='products')
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'