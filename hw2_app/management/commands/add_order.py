from django.core.management.base import BaseCommand
from hw2_app.models import Order, Product, Customer


class Command(BaseCommand):
    help = "Add new order"

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='Customer ID')
        parser.add_argument('products_id', nargs='+', type=str, help='IDs products')

    def handle(self, *args, **kwargs):
        customer_id = kwargs.get('customer_id')
        customer = Customer.objects.get(pk=int(customer_id))
        order = Order(customer=customer, total_price=0)
        order.save()
        total_sum = 0
        products = kwargs.get('products_id')
        for i in range(len(products)):
            product_id = products[i]
            product = Product.objects.get(pk=int(product_id))
            product.quantity -= 1
            product.save()
            total_sum += product.price
            order.products.add(product)
            order.save()
            i += 1
        order.total_price = total_sum
        order.save()
        self.stdout.write(f'{order}')
