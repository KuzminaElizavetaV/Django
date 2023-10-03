from django.core.management.base import BaseCommand
from hw2_app.models import Order


class Command(BaseCommand):
    help = "Find order by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Find order by ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
        