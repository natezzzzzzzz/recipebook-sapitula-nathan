from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeInline(admin.StackedInline):
    model = RecipeImage
    can_delete = False

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on', 'updated_on')
    model = Recipe
    inlines = [RecipeInline, ]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete= False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
