from decimal import Decimal
from random import randrange

from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **options):
        for i in range(10):
            order = shopapp_models.Order()
            order.customer = get_object_or_404(shopapp_models.Customer, pk=randrange(1, 10))
            order.product = get_object_or_404(shopapp_models.Product, pk=randrange(1, 10))
            order.total_price = Decimal(i + 1)
            order.total = i + 1
            order.save()

        self.stdout.write(f"save complite")
