from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.http import HttpResponse



def recipe_list(request):
    recipes = Recipe.objects.all()  
    context = {'recipes': recipes}
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


