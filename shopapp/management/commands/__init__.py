from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Print hello world!"

    def handle(self, *args, **options):
        self.stdout.write("Hello world")
