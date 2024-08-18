from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('find/', views.find, name="find"),
    path('generate/', views.generate, name="generate"),
    path('recipe/', views.recipe, name="recipe"),
    path('generateRecipe/', views.generateRecipe, name="generateRecipe"),
    path('save_favorite/', views.save_favorite, name="save_favorite"),
    path('ingredient/', views.findIngredient, name="ingredient"),
    path('ingredientRecipe/', views.ingredientRecipe, name="ingredientRecipe")
]