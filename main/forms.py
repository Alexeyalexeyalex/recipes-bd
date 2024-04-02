from django import forms
from .models import Categories, Recipes


class RecipesForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    cooking_steps = forms.CharField(widget=forms.Textarea)
    cooking_time = forms.IntegerField()
    image = forms.ImageField()
    author = forms.CharField(max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Categories.objects.all())

class CategoriesForm(forms.Form):
    name = forms.CharField(max_length=100)


class CommentForm(forms.Form):
    recipes = forms.ModelChoiceField(queryset=Recipes.objects.all())
    category = forms.ModelChoiceField(queryset=Categories.objects.all())



