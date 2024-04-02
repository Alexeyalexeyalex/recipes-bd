from django.core.management.base import BaseCommand
from main.models import RecipesCategories, Categories, Recipes
from django.utils import lorem_ipsum
from random import choice, randint

class Command(BaseCommand):
    help = "Create RecipesCategories"

    def handle(self, *args, **kwargs):

        recipes = Recipes.objects.all()
        categories = Categories.objects.all()

        for i in range(10):
            recipes_categories = RecipesCategories(
                recipes = choice(recipes),
                category = choice(categories),)
            recipes_categories.save()