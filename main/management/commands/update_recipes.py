from django.core.management.base import BaseCommand
from main.models import Recipes



class Command(BaseCommand):
    help = "Update Recipes by id."

    def add_arguments(self, parser):
            parser.add_argument('pk', type=int, help='Recipes ID')
            parser.add_argument('name', type=str, help='Recipes name')
            parser.add_argument('description', type=str, help='Recipes description')
            parser.add_argument('cooking_steps', type=str, help='Recipes cooking_steps')
            parser.add_argument('cooking_time', type=int, help='Recipes cooking_time')
            parser.add_argument('image', type=str, help='Recipes image')
            parser.add_argument('author', type=str, help='Recipes author')
            parser.add_argument('ingredients', type=str, help='Recipes ingredients')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        cooking_steps = kwargs.get('cooking_steps')
        cooking_time = kwargs.get('cooking_time')
        image = kwargs.get('image')
        author = kwargs.get('author')
        ingredients = kwargs.get('ingredients')

        recipes = Recipes.objects.filter(pk=pk).first()
        recipes.name = name
        recipes.description = description
        recipes.cooking_steps = cooking_steps
        recipes.cooking_time = cooking_time
        recipes.image = image
        recipes.author = author
        recipes.ingredients = ingredients


        recipes.save()

