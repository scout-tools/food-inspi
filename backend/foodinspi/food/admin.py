from django.contrib import admin

from .models import MeasuringUnit, Price, Tag, TagCategory, Ingredient, Recipe, Portion, Retailer, Package, RecipeItem

from django.contrib import admin
from django.contrib.auth.models import User, Group


# We add this so no authentication is needed when entering the admin site
class AccessUser(object):
    has_module_perms = has_perm = __getattr__ = lambda s, *a, **kw: True


admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

# We add this to remove the user/group admin in the admin site as there is no user authentication
admin.site.unregister(User)
admin.site.unregister(Group)

# Create superuser for admin use in case it doesn't exist
try:
    User.objects.get_by_natural_key('admin')
except User.DoesNotExist:
    User.objects.create_superuser('admin', 'admin@optibus.co', '123456')

admin.site.register(MeasuringUnit)
admin.site.register(Tag)
admin.site.register(TagCategory)


class PortionInline(admin.TabularInline):
    model = Portion
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
        'fruit_factor')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    readonly_fields = (
        'nutri_points',
        'nutri_class',
        'fruit_factor',
        'ndb_number',
        'major_class',)
    search_fields = ['name']
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
    list_display = (
        'name',
        'weight_g',
        'energy_kj',
        'carbohydrate_g',
        'fat_g',
        'protein_g',
        'fibre_g',
        'nutri_class',
    )
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
    readonly_fields = ('weight_package_g',)

    inlines = [
        PriceInline,
    ]


admin.site.register(Retailer)
