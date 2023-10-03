from django.core.management.base import BaseCommand
from hw2_app.models import Customer


class Command(BaseCommand):
    help = "Update customer"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=int, help='Customer ID')
        parser.add_argument('-n', '--name', type=str, help='Customer name', required=False)
        parser.add_argument('-e', '--email', type=str, help='Customer email', required=False)
        parser.add_argument('-p', '--phone', type=str, help='Customer phone', required=False)
        parser.add_argument('-a', '--address', type=str, help='Customer address', required=False)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('id')
        client = Customer.objects.filter(pk=pk).first()
        if kwargs.get('name'):
            client.name = kwargs.get('name')
        if kwargs.get('email'):
            client.email = kwargs.get('email')
        if kwargs.get('phone'):
            client.phone = kwargs.get('phone')
        if kwargs.get('address'):
            client.address = kwargs.get('address')
        client.save()
        self.stdout.write(f'{client}')
