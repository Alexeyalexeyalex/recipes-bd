from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from random import choices, randint
from main.models import Recipes, Categories, RecipesCategories
from .forms import RecipesForm, CategoriesForm
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import STATIC_ROOT


def recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'main/recipes.html', {'recipes':recipes})

def five_recipes(request):

    recipes = choices(Recipes.objects.all(), k=5)
    print(type(recipes[0]))
    return render(request, 'main/five_recipes.html', {'recipes':recipes})


def recipe(request, recipe_id):
    recipes = Recipes.objects.get(id=recipe_id)
    recipe = {
        "name": recipes.name,
        "image": recipes.image,
        "author": recipes.author,
        "cooking_time": recipes.cooking_time,
        "ingredients": recipes.ingredients,
        "description": recipes.description,
        "cooking_steps": recipes.cooking_steps
    }

    return render(request, 'main/recipe.html', {'recipe':recipe})


def recipe_form(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipes.objects.create(
                name=data['name'],
                description=data['description'],
                cooking_steps=data['cooking_steps'],
                cooking_time=data['cooking_time'],
                image=f"main/{data['image'].name}/",
                ingredients=data['ingredients'],
                author=data['author'],)
            category = Categories.objects.create(
                name=data['category'],)
            RecipesCategories.objects.create(
                recipes=recipe,
                category=category,)
            fs = FileSystemStorage(location='main/static/main/', base_url='/main')
            fs.save(data['image'].name, data['image'])
            return redirect('recipe_form')
    else:
        form = RecipesForm()
    return render(request, 'main/recipe_form.html', {'form': form})