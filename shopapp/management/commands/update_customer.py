from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Update customer"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Customer ID")
        parser.add_argument("phone", type=str, help="Customer ID")

    def handle(self, *args, **options):
        pk = options["pk"]
        phone = options["phone"]
        customer = shopapp_models.Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.phone = phone
            customer.save()
            self.stdout.write(f"{customer} номер телефона изменен: {phone}")
