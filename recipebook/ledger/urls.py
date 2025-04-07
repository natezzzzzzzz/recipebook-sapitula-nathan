from django.urls import path
from .views import *

urlpatterns = [
    path("recipes/list", recipeList, name="recipeList"),
    path("recipe/<int:num>", recipe, name="recipe"),
    path("recipe/add", recipeAdd, name="recipeAdd"),
]
