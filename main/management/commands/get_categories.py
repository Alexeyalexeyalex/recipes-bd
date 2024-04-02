from django.core.management.base import BaseCommand
from main.models import Categories


class Command(BaseCommand):
    help = "Get Categories"

    def handle(self, *args, **kwargs):
        categories = Categories.objects.all()

        return str(categories)