from django.urls import path

from .views import RecipeListView, RecipeDetailView, CreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes_list'),
    path('<int:recipe_id>/', RecipeDetailView.as_view()),
    path('create/', CreateView.as_view())
]
