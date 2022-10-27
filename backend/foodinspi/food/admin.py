from django.contrib import admin

from .models import MeasuringUnit, Price, Tag, TagCategory, Ingredient, Recipe, Portion, Retailer, Package, RecipeItem, Hint

from django.contrib import admin
from django.contrib.auth.models import User, Group


admin.site.register(MeasuringUnit)
admin.site.register(Tag)
admin.site.register(TagCategory)


class PortionInline(admin.TabularInline):
    model = Portion
    ordering = ['name']
    readonly_fields = (
        'weight_g',
        'energy_kj',
        'protein_g',
        'fat_g',
        'fat_sat_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
        'salt_g',
        'fructose_g',
        'lactose_g',
        'price_per_kg',
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    readonly_fields = (
        'nutri_points',
        'nutri_class',
        'fruit_factor',
        'ndb_number',
        'nutri_points_energy_kj',
        'nutri_points_sugar_g',
        'nutri_points_salt_g',
        'nutri_points_fibre_g',
        'nutri_points_fat_sat_g',
        'nutri_points_protein_g',
    )
    search_fields = ['name']
    ordering = ['name']
    list_display = (
        'name',
        'description',
        'nutri_points',
        'major_class',
    )
    list_filter = ('major_class', 'nutri_class',)

    inlines = [
        PortionInline,
    ]


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
        'fat_sat_g',
        'sugar_g',
        'carbohydrate_g',
        'fibre_g',
        'fructose_g',
        'lactose_g',
        'nutri_points_energy_kj',
        'nutri_points_sugar_g',
        'nutri_points_salt_g',
        'nutri_points_fibre_g',
        'nutri_points_fat_sat_g',
        'nutri_points_protein_g',
        'fruit_factor',
        'price_per_kg',
        'price',
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ordering = ['name']
    readonly_fields = (
        'hints',
        'nutri_class',
        'weight_g',
        'nutri_points',
        'energy_kj',
        'protein_g',
        'fat_g',
        'fat_sat_g',
        'sugar_g',
        'sodium_mg',
        'carbohydrate_g',
        'fibre_g',
        'fruit_factor',
        'salt_g',
        'fructose_g',
        'lactose_g',
        'price',
    )
    list_display = (
        'name',
        'weight_g',
        'energy_kj',
        'carbohydrate_g',
        'fat_g',
        'protein_g',
        'fibre_g',
        'nutri_class',
        'price',
        'get_hints'
    )
    list_filter = ('meal_type',)

    def get_hints(self, obj):
        return "\n, ".join([p.name for p in obj.hints.all()])

    inlines = [
        RecipeItemInline,
    ]


class PriceInline(admin.TabularInline):
    model = Price
    readonly_fields = (
        'price_per_kg',
    )


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    ordering = ['portion']
    readonly_fields = (
        'weight_package_g',
        'price_per_kg',)

    inlines = [
        PriceInline,
    ]


admin.site.register(Retailer)


@admin.register(Hint)
class EventModuleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description',]
    list_display = ('name', 'description', 'parameter',
                    'min_max', 'value', 'hint_level',)
    search_fields = ('name', 'description',)
    list_filter = ('parameter',)
