from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.

def index(request):
    recipe = Recipe.objects.all()
    return render(request, 'index.html',{'recipe':recipe})


def add_recipe(request):
    if request.method == 'POST':
        new_recipe = Recipe(
        name = request.POST.get('name'),
        ingredients = request.POST.get('ingredients'),
        instructions = request.POST.get('instructions'),
        )
        new_recipe.save()
        return redirect('index')
    return render(request,'add.html')

def info(request,name):
    recipe = Recipe.objects.get(name=name)
    return render(request, 'info.html', {'recipe':recipe})

def delete(request,name):
    recipe = Recipe.objects.get(name=name)
    recipe.delete()
    return redirect('index')

def edit(request, name):
    if request.method == 'POST':
        recipe = Recipe.objects.get(name=name)
        recipe.name = request.POST.get('name')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions')
        recipe.save()
        return redirect('index')
    return render(request,'edit.html')


