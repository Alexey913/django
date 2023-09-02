from django.core.management.base import BaseCommand
from hw_app.models import Goods
from decimal import Decimal


class Command(BaseCommand):
    help = "Create goods"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Goods title')
        parser.add_argument('description', type=str, help='Goods description')
        parser.add_argument('price', type=Decimal, help='Goods price')
        parser.add_argument('quantity', type=int, help='Goods quantity')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        goods = Goods(title=title,
                      description=description,
                      price=price,
                      quantity=quantity,
                      )
        goods.save()
        self.stdout.write(f'Создана запись {goods}')
