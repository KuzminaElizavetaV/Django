from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Update product"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=int, help='Product ID')
        parser.add_argument('-n', '--name', type=str, help='Product name', required=False)
        parser.add_argument('-d', '--description', type=str, help='Product description', required=False)
        parser.add_argument('-p', '--price', type=float, help='Product price', required=False)
        parser.add_argument('-q', '--quantity', type=int, help='Product quantity', required=False)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('id')
        product = Product.objects.filter(pk=pk).first()
        if kwargs.get('name'):
            product.name = kwargs.get('name')
        if kwargs.get('description'):
            product.description = kwargs.get('description')
        if kwargs.get('price'):
            product.price = kwargs.get('price')
        if kwargs.get('quantity'):
            product.quantity = kwargs.get('quantity')
        product.save()
        self.stdout.write(f'{product}')
