from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.id)])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
