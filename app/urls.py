from django.contrib import admin
from django.urls import path, include

from recipes.views import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("admin/", admin.site.urls),
    path("recipes/", include("recipes.urls")),
]
