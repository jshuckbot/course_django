from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Delete customer"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Customer ID")

    def handle(self, *args, **options):
        pk = options["pk"]
        customer = shopapp_models.Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.delete()
            self.stdout.write(f"{customer} удален")
