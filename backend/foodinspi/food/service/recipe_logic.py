from food import models as food_models
from django.db.models import Sum
from food.service.nutri_lib import Nutri


class RecipeModule:
    def recalculate_recipe(self, recipe_id):
        recipe_item_set = food_models.RecipeItem.objects.filter(
            recipe=recipe_id)

        for recipe_item in recipe_item_set:
            NutriClass = Nutri()
            recipe_item.weight_g = round(
                recipe_item.portion.weight_g * recipe_item.quantity, 2)
            recipe_item.energy_kj = round(
                recipe_item.portion.energy_kj * recipe_item.quantity, 2)
            recipe_item.protein_g = round(
                recipe_item.portion.protein_g * recipe_item.quantity, 2)
            recipe_item.fat_g = round(
                recipe_item.portion.fat_g * recipe_item.quantity, 2)
            recipe_item.saturated_fatty_acids_g = round(
                recipe_item.portion.saturated_fatty_acids_g * recipe_item.quantity, 2)
            recipe_item.sugar_g = round(
                recipe_item.portion.sugar_g * recipe_item.quantity, 2)
            recipe_item.sodium_mg = round(
                recipe_item.portion.sodium_mg * recipe_item.quantity, 2)
            recipe_item.carbohydrate_g = round(
                recipe_item.portion.carbohydrate_g * recipe_item.quantity, 2)
            recipe_item.fibre_g = round(
                recipe_item.portion.fibre_g * recipe_item.quantity, 2)
            recipe_item.save()

        recipe_set = food_models.Recipe.objects.filter(id=recipe_id).first()
        print(recipe_set)

        recipe_item_set = food_models.RecipeItem.objects.filter(
            recipe=recipe_id)

        recipe_weight_g = recipe_item_set.aggregate(
            sum=Sum('weight_g'))['sum'] or 0

        print(recipe_weight_g)

        for recipe_item in recipe_item_set:
            recipe_item.weight_recipe_factor = round(
                recipe_item.weight_g / recipe_weight_g, 3)
            recipe_item.nutri_points = round(
                recipe_item.portion.ingredient.nutri_points * recipe_item.weight_recipe_factor, 1)
            recipe_item.nutri_class = NutriClass.get_nutri_class(
                'solid', recipe_item.portion.ingredient.nutri_points)
            print(recipe_item.nutri_points)
            recipe_item.save()
