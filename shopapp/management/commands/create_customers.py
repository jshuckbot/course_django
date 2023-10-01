from django.core.management import BaseCommand

from shopapp import models as shopapp_models


class Command(BaseCommand):
    help = "Create Customer"

    def handle(self, *args, **options):
        customer = shopapp_models.Customer()
        customer.first_name = "John"
        customer.email = "test@test.ru"
        customer.phone = "9433330229"
        customer.address = "Testogorsk"
        customer.save()

        self.stdout.write(f"{customer}")
