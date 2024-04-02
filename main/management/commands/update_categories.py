from django.core.management.base import BaseCommand
from main.models import Categories



class Command(BaseCommand):
    help = "Update Categories by id."

    def add_arguments(self, parser):
            parser.add_argument('pk', type=int, help='Categories ID')
            parser.add_argument('name', type=str, help='Categories name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')

        categories = Categories.objects.filter(pk=pk).first()
        categories.name = name
        categories.save()

