from django.core.management.base import BaseCommand
from main.models import RecipesCategories


class Command(BaseCommand):
    help = "Get RecipesCategories"

    def handle(self, *args, **kwargs):
        recipes_categories = RecipesCategories.objects.all()

        return str(recipes_categories)