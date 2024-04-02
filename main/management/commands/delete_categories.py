from django.core.management.base import BaseCommand
from main.models import Categories


class Command(BaseCommand):
    help = "Delete Categories by id."


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
    
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        categories = Categories.objects.filter(pk=pk).first()
        if categories is not None:
            categories.delete()
        self.stdout.write(f'{categories}')