from django.core.management.base import BaseCommand
from main.models import RecipesCategories


class Command(BaseCommand):
    help = "Delete RecipesCategories by id."


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
    
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        recipes_categories = RecipesCategories.objects.filter(pk=pk).first()
        if recipes_categories is not None:
            recipes_categories.delete()
        self.stdout.write(f'{recipes_categories}')