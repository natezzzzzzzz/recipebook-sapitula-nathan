from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def recipeList(request):
    recipe_list = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes': recipe_list})

@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(id=num)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) if recipe else []
    return render(request, "recipeEntry.html", {'recipe': recipe, 'ingredients': ingredients})

@login_required
def recipeAdd(request):

    recipeForm = RecipeForm()
    recipeIngredientForm = RecipeIngredientForm()
    ingredientForm = IngredientForm()

    if request.method == 'POST':

        if 'submitRecipe' in request.POST:
            recipeForm = RecipeForm(request.POST)
            if recipeForm.is_valid():
                recipeForm.save()

        elif 'submitRecipeIngredient' in request.POST:
            recipeIngredientForm = RecipeIngredientForm(request.POST)
            if recipeIngredientForm.is_valid():
                recipeIngredientForm.save()
        
        elif 'submitIngredient' in request.POST:
            ingredientForm = IngredientForm(request.POST)
            if ingredientForm.is_valid():
                ingredientForm.save()

    return render(request, "recipeAdd.html", {'recipeForm': recipeForm, 'recipeIngredientForm': recipeIngredientForm, 'ingredientForm': ingredientForm})

@login_required
def imageAdd(request, num):
    recipe = Recipe.objects.get(id=num)
    imageForm = ImageForm()

    if request.method == 'POST':
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            image = imageForm.save(commit=False)
            image.recipe = recipe
            image.save()

    return render(request, "imageAdd.html", {'imageForm': imageForm, 'recipe': recipe})