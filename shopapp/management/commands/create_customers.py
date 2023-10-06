from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Create Customer"

    def handle(self, *args, **options):
        for i in range(10):
            customer = shopapp_models.Customer()
            customer.first_name = f"name{i}"
            customer.email = f"test@test{i}.ru"
            customer.phone = f"94333{i}229"
            customer.address = f"Testogorsk{i}"
            customer.save()

        self.stdout.write(f"save complite")
