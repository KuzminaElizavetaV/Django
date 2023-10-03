from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Add new product"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='Product Name')
        parser.add_argument('-d', '--description', type=str, help='Product Description', required=False)
        parser.add_argument('-p', '--price', type=float, help='Product Price')
        parser.add_argument('-q', '--quantity', type=int, help='Product Quantity', required=False)

    def handle(self, *args, **kwargs):
        product = Product(name=kwargs.get('name'),
                          price=kwargs.get('price'))
        if kwargs.get('description'):
            product.description = kwargs.get('description')
        if kwargs.get('quantity'):
            product.quantity = kwargs.get('quantity')
        product.save()
        self.stdout.write(f'{product}')
