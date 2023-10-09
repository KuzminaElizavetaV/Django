from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100, default='Unknown')
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Клиент: {self.name}, {self.email}, {self.phone}, {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, цена: {self.price} руб.'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('order', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Заказ № {self.pk} на общую сумму {self.total_price} руб.\n' \
               f'Товары: {list(map(str, self.products.all()))}\n{self.customer}'
