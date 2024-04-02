from django.core.management.base import BaseCommand
from main.models import Categories
from django.utils import lorem_ipsum
from random import choice


class Command(BaseCommand):
    help = "Create category"

    def handle(self, *args, **kwargs):
        for i in range(30):
            categories = Categories(
                name = choice(lorem_ipsum.WORDS),)
            
            categories.save()
