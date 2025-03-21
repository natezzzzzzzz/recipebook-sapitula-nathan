from django.shortcuts import render
from .models import *

def recipeList(request):
    recipe_list = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes': recipe_list})

def recipe(request, num=1):
    recipe = Recipe.objects.get(id=num)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) if recipe else []
    return render(request, "recipeEntry.html", {'recipe': recipe, 'ingredients': ingredients})
