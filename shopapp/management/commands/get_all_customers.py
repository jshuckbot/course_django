from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Get all customers"

    def handle(self, *args, **options):
        customers = shopapp_models.Customer.objects.all()
        for customer in customers:
            self.stdout.write(f"{customer}")
