from django.db import models


class TimeStampMixin(models.Model):
    """Время создания и обновления рецептов"""

    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления", auto_now=True)

    class Meta:
        abstract = True


class Ingredient(TimeStampMixin):
    """Ингредиенты"""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class Recipe(TimeStampMixin):
    """Рецепт: название, описание, ингредиенты, фотография"""

    heading = models.CharField("Название", max_length=50, unique=True)
    text = models.TextField("Рецепт")
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.heading
