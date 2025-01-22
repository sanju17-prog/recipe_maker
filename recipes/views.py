from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

RECIPES_URL = '/recipes/'
LOGIN_URL = '/recipes/login'
# Create your views here.
@login_required(login_url=LOGIN_URL)
def recipes(request):
    if request.method == 'POST':
        return create_recipe(request)
    
    queryset = Recipe.objects.all()
    if searched_value:= request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = searched_value)
    context = {'recipes': queryset}
    return render(request, 'recipes/recipes.html', context)


@login_required(login_url=LOGIN_URL)
def create_recipe(request):
    data = request.POST
    recipe_name = data['recipe_name']
    recipe_description = data['recipe_description']
    recipe_image = request.FILES.get('recipe_image')
    Recipe.objects.create(
        recipe_name=recipe_name, 
        recipe_description=recipe_description, 
        recipe_image = recipe_image
    )
    return redirect(RECIPES_URL)

@login_required(login_url=LOGIN_URL)
def delete_recipe(request, slug):
    if request.method == 'GET':
        print("reached here")
        queryset = get_object_or_404(Recipe, slug = slug)
        queryset.delete()
        return redirect(RECIPES_URL)
    return HttpResponseBadRequest("Invalid Request method")

@login_required(login_url=LOGIN_URL)
def update_recipe(request, slug):
    queryset = get_object_or_404(Recipe, slug = slug)
    if request.method == 'POST':
        return update_recipe_from_post(request, queryset)
    context = {'recipe': queryset}
    return render(request, 'recipes/update_recipe.html', context)

@login_required(login_url=LOGIN_URL)
def update_recipe_from_post(request, queryset):
    data = request.POST
    queryset.recipe_name = data.get('recipe_name')
    queryset.recipe_description = data.get('recipe_description')
    
    if recipe_image := request.FILES.get('recipe_image'):
        queryset.recipe_image = recipe_image

    queryset.save()
    return redirect(RECIPES_URL)