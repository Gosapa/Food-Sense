from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('find/', views.find, name="find"),
    path('generate/', views.generate, name="generate"),
    path('recipe/', views.recipe, name="recipe"),
]
