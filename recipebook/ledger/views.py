from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def recipeList(request):
    recipe_list = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes': recipe_list})

@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(id=num)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) if recipe else []
    return render(request, "recipeEntry.html", {'recipe': recipe, 'ingredients': ingredients})
