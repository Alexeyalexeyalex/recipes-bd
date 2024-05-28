"""
Файл для добавления моделей на страницу администратора
"""
from django.contrib import admin

from .models import Recipes, Categories, RecipesCategories

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    """Структурирует информацию о рецептах и добавляет фильтр по автору"""
    list_display = ['name','cooking_steps', 'cooking_time', 'ingredients', 'author', 'author',
                    'image','description']
    list_filter = ['author']
    fieldsets = (('Информация о рецепте', {'fields':['name','cooking_steps',
                                                     'cooking_time', 'ingredients']}),
                 ('Дополнительная информация', {'fields':['image','description']}),
                 ('Автор', {'fields':['author']}),)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Структурирует информацию о категориях"""
    list_display = ['name']
    fieldsets = (('Информация о категории', {'fields':['name']}),)


@admin.register(RecipesCategories)
class RecipesCategoriesAdmin(admin.ModelAdmin):
    """Структурирует информацию о смежной таблице рецептов и категорий"""
    list_display = ['recipes', 'category']
