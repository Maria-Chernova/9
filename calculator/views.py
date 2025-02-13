from django.shortcuts import render
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def res(request, recipe_name):
    recipe = DATA.get(recipe_name)
    servings = request.GET.get('servings', 1)
    servings = int(servings)
    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': adjusted_recipe
    }
    return render(request, 'calculator/index.html', context)

