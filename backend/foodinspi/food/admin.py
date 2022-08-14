from django.contrib import admin

from .models import MeasuringUnit, Price, Tag, TagCategory, Ingredient, Recipe, Portion, Retailer, Package, RecipeItem


admin.site.register(MeasuringUnit)
admin.site.register(Price)
admin.site.register(Tag)
admin.site.register(TagCategory)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    readonly_fields = ('nutri_points',)
    search_fields = ['tags']
    list_display = (
        'name',
        'description',
    )
    list_filter = ('name',)


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    readonly_fields = (
        'weight_recipe_factor',
        'weight_g',
        'nutri_points',
        'nutri_class',
        'energy_kj',
        'protein_g',
        'fat_g',
        'saturated_fatty_acids_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'nutri_class',
        'weight_g',
        'nutri_points',
        'energy_kj',
        'protein_g',
        'fat_g',
        'saturated_fatty_acids_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
    )

    inlines = [
        RecipeItemInline,
    ]


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    readonly_fields = ('weight_package_g',)


admin.site.register(Retailer)


@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'weight_g',
        'energy_kj',
        'protein_g',
        'fat_g',
        'saturated_fatty_acids_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
    )


@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    readonly_fields = (
        'weight_recipe_factor',
        'weight_g',
        'nutri_points',
        'nutri_class',
        'energy_kj',
        'protein_g',
        'fat_g',
        'saturated_fatty_acids_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
    )
