from django.core.management.base import BaseCommand
from hw2_app.models import Order


class Command(BaseCommand):
    help = "Find all orders by client ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        customer_id = kwargs.get('pk')
        orders = Order.objects.filter(customer=int(customer_id)).all()
        for order in orders:
            self.stdout.write(f'\n{order}\n--------------------------------------')
