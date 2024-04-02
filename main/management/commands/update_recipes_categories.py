from django.core.management.base import BaseCommand
from main.models import RecipesCategories, Recipes, Categories



class Command(BaseCommand):
    help = "Update RecipesCategories by id."

    def add_arguments(self, parser):
            parser.add_argument('pk', type=int, help='RecipesCategories ID')
            parser.add_argument('recipes', type=str, help='recipes ID')
            parser.add_argument('categories', type=str, help='Categories ID')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        recipes_id = kwargs.get('recipes')
        categories_id = kwargs.get('categories')

        recipes = Recipes.objects.filter(pk=recipes_id).first()
        categories = Categories.objects.filter(pk=categories_id).first()

        recipes_categories = RecipesCategories.objects.filter(pk=pk).first()
        recipes_categories.recipes = recipes
        recipes_categories.categories = categories
        recipes_categories.save()

