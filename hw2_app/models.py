from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=100, default='Unknown', verbose_name='Адрес')
    reg_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(default=1, verbose_name='Количество')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    image = models.ImageField(default=None, blank=True, verbose_name='Изображение')
    update_date = models.DateField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name}, цена: {self.price} руб.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Общая стоимость')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата оформления')

    def get_absolute_url(self):
        return reverse('order', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Заказ № {self.pk}'  # сумму {self.total_price} руб.\n'
        # f'Товары: {list(map(str, self.products.all()))}\n{self.customer}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
