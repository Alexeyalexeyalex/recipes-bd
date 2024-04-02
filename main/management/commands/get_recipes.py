from django.core.management.base import BaseCommand
from main.models import Recipes


class Command(BaseCommand):
    help = "Get Recipes"

    def handle(self, *args, **kwargs):
        recipes = Recipes.objects.all()

        return str(recipes)