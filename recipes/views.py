from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views import View

from .forms import CreateForm
from .models import Recipe, Ingredient


class HomeView(View):

    @staticmethod
    def get():
        return redirect(reverse('recipes_list'))


class RecipeListView(View):
    """Список рецептов"""

    def get(self, request):
        recipe_name = self.request.GET.get('recipe')
        ingredients_query = self.request.GET.getlist('ingredients')
        recipes_list = Recipe.objects.all()
        if recipe_name:
            recipes_list = recipes_list.filter(heading__icontains=recipe_name)
        if ingredients_query and 'Все ингредиенты' not in ingredients_query:
            recipes_list = recipes_list.filter(ingredients__name__in=ingredients_query).distinct()

        context = {'recipes_list': recipes_list, 'ingredients_list': Ingredient.objects.all().order_by('name')}
        return render(request, 'recipes/recipelist.html', context)


class RecipeDetailView(View):
    """Детали рецепта"""

    def get(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404('Такого рецепта не существует')
        return render(request, 'recipes/recipedetail.html', {'recipe': recipe})


class CreateView(View):
    """Создание рецепта"""

    def get(self, request):
        form = CreateForm()
        return render(request, 'recipes/create_recipe.html', {'form': form})

    def post(self, request):
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            recipe = Recipe.objects.get(heading=form.cleaned_data['heading'])
            new_ingredients = form.cleaned_data['additional_ingredients'].split(',')
            for each in new_ingredients:
                try:
                    new_ingredient = Ingredient.objects.get(name=each)
                except Ingredient.DoesNotExist:
                    new_ingredient = Ingredient(name=each)
                    new_ingredient.save()
                if new_ingredient not in recipe.ingredients.all():
                    recipe.ingredients.add(new_ingredient)
                    recipe.save()
            return redirect('recipes_list')
        return render(request, 'recipes/create_recipe.html', {'form': form})
