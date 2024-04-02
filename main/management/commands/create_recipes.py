from django.core.management.base import BaseCommand
from main.models import Recipes
from django.utils import lorem_ipsum
from random import randint, choice


class Command(BaseCommand):
    help = "Create recipes"

    def handle(self, *args, **kwargs):
        for i in range(10):
            recipes = Recipes(
                name = choice(lorem_ipsum.WORDS),
                description = ". ".join(lorem_ipsum.paragraphs(5, common=False)),
                cooking_steps = ". ".join(lorem_ipsum.paragraphs(10, common=False)),
                cooking_time = randint(15,120),
                image = "",
                author = choice(lorem_ipsum.WORDS),
                ingredients = "".join(lorem_ipsum.paragraphs(1, common=False)),)

            
            recipes.save()




