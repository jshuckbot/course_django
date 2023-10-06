from decimal import Decimal

from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Create Product"

    def handle(self, *args, **options):
        for i in range(10):
            product = shopapp_models.Product()
            product.name = f"product{i}"
            product.description = f"desc{i}"
            product.price = Decimal(i + 1)
            product.total = i + 1
            product.save()

        self.stdout.write(f"save complite")
