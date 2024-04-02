from django.core.management.base import BaseCommand
from main.models import Recipes


class Command(BaseCommand):
    help = "Delete Recipes by id."


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
    
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        recipes = Recipes.objects.filter(pk=pk).first()
        if recipes is not None:
            recipes.delete()
        self.stdout.write(f'{recipes}')