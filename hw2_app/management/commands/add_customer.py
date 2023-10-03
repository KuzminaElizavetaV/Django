from django.core.management.base import BaseCommand
from hw2_app.models import Customer


class Command(BaseCommand):
    help = "Add new customer"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='Customer Name')
        parser.add_argument('-e', '--email', type=str, help='Customer Email')
        parser.add_argument('-p', '--phone', type=str, help='Customer Phone')
        parser.add_argument('-a', '--address', type=str, help='Client Address', required=False)

    def handle(self, *args, **kwargs):
        customer = Customer(name=kwargs.get('name'),
                            email=kwargs.get('email'),
                            phone=kwargs.get('phone'))
        if kwargs.get('address'):
            customer.address = kwargs.get('address')
        customer.save()
        self.stdout.write(f'{customer}')
