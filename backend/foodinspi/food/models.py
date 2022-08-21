from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from food.service.nutri_lib import Nutri
from food.service.recipe_logic import RecipeModule


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class NutrientsMixin(models.Model):
    energy_kj = models.FloatField(default=0)
    protein_g = models.FloatField(default=0)
    fat_g = models.FloatField(default=0)
    saturated_fatty_acids_g = models.FloatField(default=0)
    sugar_g = models.FloatField(default=0)
    sodium_mg = models.FloatField(default=0)
    fruit_factor = models.FloatField(default=0, blank=True)
    carbohydrate_g = models.FloatField(default=0)
    fibre_g = models.FloatField(default=0)

    class Meta:
        abstract = True


class MeasuringUnit(TimeStampMixin):

    class Units(models.TextChoices):
        VOLUME = 'ml', 'Millilitter'
        MASS = 'g', 'Gramm'

    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    quantity = models.FloatField()
    unit = models.CharField(
        max_length=2,
        choices=Units.choices,
        default=Units.MASS,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class TagCategory(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    is_ingredient = models.BooleanField(default=True)
    is_recipe = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Tag(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    tag_category = models.ForeignKey(
        TagCategory, on_delete=models.PROTECT, null=True)
    is_ingredient = models.BooleanField(default=True)
    is_recipe = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Ingredient(TimeStampMixin, NutrientsMixin):
    class PhysicalViscosityChoices(models.TextChoices):
        SOLID = 'solid', 'Essen'
        BEVERAGE = 'beverage', 'Getränk'

    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    physical_density = models.FloatField(default=1)
    physical_viscosity = models.CharField(
        max_length=10,
        choices=PhysicalViscosityChoices.choices,
        default=PhysicalViscosityChoices.SOLID,
    )
    tags = models.ManyToManyField(Tag, related_name='IngredientTags', blank=True)
    fdc_id = models.IntegerField(null=True, blank=True)

    # readonly
    nutri_points = models.IntegerField(null=True, blank=True)
    nutri_class = models.FloatField(null=True, blank=True)
    ndb_number = models.IntegerField(null=True, blank=True)
    major_class = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.description}'

    def __repr__(self):
        return self.__str__()


class Portion(TimeStampMixin, NutrientsMixin):
    name = models.CharField(max_length=255)
    measuring_unit = models.ForeignKey(
        MeasuringUnit, on_delete=models.PROTECT, blank=True, null=True, default=3)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.PROTECT, default=1)
    quantity = models.FloatField(default=1)
    rank = models.IntegerField(default=1)
    # readonly
    weight_g = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        is_g = self.measuring_unit.unit == 'g'
        if is_g:
            self.weight_g = self.measuring_unit.quantity * self.quantity
        else:
            self.weight_g = self.measuring_unit.quantity * \
                self.quantity * self.ingredient.physical_density

        # Nutrients
        self.energy_kj = round(
            self.ingredient.energy_kj * self.weight_g / 100, 2)
        self.protein_g = round(
            self.ingredient.protein_g * self.weight_g / 100, 2)
        self.fat_g = round(self.ingredient.fat_g * self.weight_g / 100, 2)
        self.saturated_fatty_acids_g = round(
            self.ingredient.saturated_fatty_acids_g * self.weight_g / 100, 2)
        self.sugar_g = round(self.ingredient.sugar_g * self.weight_g / 100, 2)
        self.sodium_mg = round(
            self.ingredient.sodium_mg * self.weight_g / 100, 2)
        self.carbohydrate_g = round(
            self.ingredient.carbohydrate_g * self.weight_g / 100, 2)
        self.fibre_g = round(self.ingredient.fibre_g * self.weight_g / 100, 2)

        super(Portion, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} / {self.quantity} {self.measuring_unit}'

    def __repr__(self):
        return self.__str__()


class Recipe(TimeStampMixin, NutrientsMixin):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, related_name='RecipeTags', blank=True)

    # readonly
    nutri_class = models.FloatField(null=True, blank=True)
    nutri_points = models.FloatField(null=True, blank=True)
    weight_g = models.FloatField(default=1)

    def get_sum(self, name, items):
        if (items[f'{name}__sum']):
            return round(items[f'{name}__sum'], 0)
        return 0.1

    def save(self, *args, **kwargs):
        NutriClass = Nutri()
        items = RecipeItem.objects.filter(recipe=self.id).aggregate(
            Sum('weight_g'),
            Sum('energy_kj'),
            Sum('protein_g'),
            Sum('fat_g'),
            Sum('saturated_fatty_acids_g'),
            Sum('sugar_g'),
            Sum('sodium_mg'),
            Sum('carbohydrate_g'),
            Sum('fibre_g'),
            Sum('nutri_points'),
        )

        self.weight_g = self.get_sum('weight_g', items)
        self.nutri_points = self.get_sum('nutri_points', items)
        self.nutri_class = NutriClass.get_nutri_class(
            'solid', self.nutri_points)
        self.energy_kj = self.get_sum('energy_kj', items)
        self.protein_g = self.get_sum('protein_g', items)
        self.fat_g = self.get_sum('fat_g', items)
        self.saturated_fatty_acids_g = self.get_sum(
            'saturated_fatty_acids_g', items)
        self.sugar_g = self.get_sum('sugar_g', items)
        self.sodium_mg = self.get_sum('sodium_mg', items)
        self.carbohydrate_g = self.get_sum('carbohydrate_g', items)
        self.fibre_g = self.get_sum('fibre_g', items)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class RecipeItem(TimeStampMixin, NutrientsMixin):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.PROTECT, blank=True, null=True)
    portion = models.ForeignKey(Portion, on_delete=models.PROTECT)
    quantity = models.FloatField(default=1)
    # readonly
    weight_g = models.FloatField(blank=True, null=True)
    weight_recipe_factor = models.FloatField(blank=True, null=True)
    nutri_points = models.FloatField(blank=True, null=True)
    nutri_class = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.recipe} - {self.quantity} x {self.portion}'

    def __repr__(self):
        return self.__str__()


class Retailer(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Package(TimeStampMixin):
    class BrandQuantityChoises(models.TextChoices):
        OWN = 'own', 'Eigenmarke'
        BRAND = 'brand', 'Marke'
        PREMIUM = 'premium', 'Premium'

    name = models.CharField(max_length=255, blank=True)
    portion = models.ForeignKey(Portion, on_delete=models.PROTECT, null=True)
    quality = models.CharField(
        max_length=10,
        choices=BrandQuantityChoises.choices,
        default=BrandQuantityChoises.BRAND,
    )
    # readonly
    weight_package_g = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.weight_package_g = self.quantity * self.portion.weight_g
        super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}  / {self.weight_package_g} g'

    def __repr__(self):
        return self.__str__()


class Price(TimeStampMixin):
    price_eur = models.FloatField()
    retailer = models.ForeignKey(
        Retailer, on_delete=models.PROTECT, blank=True)
    package = models.ForeignKey(Package, on_delete=models.PROTECT, null=True)

    # readonly
    price_per_kg = models.FloatField(default=1)

    def save(self, *args, **kwargs):
        self.price_per_kg = round(
            self.price_eur / (self.package.weight_package_g / 1000), 2)
        super(Price, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.package} - {self.price_eur} € - {self.retailer}'

    def __repr__(self):
        return self.__str__()


# pylint: disable=unused-argument
@receiver(post_save, sender=Recipe)
def save_recipe(sender, instance: Recipe, **kwargs):
    RecipeClass = RecipeModule()
    RecipeClass.recalculate_recipe(instance.id)


# pylint: disable=unused-argument
@receiver(pre_save, sender=RecipeItem)
def save_recipe(sender, instance: RecipeItem, **kwargs):
    NutriClass = Nutri()
    instance.weight_g = round(instance.portion.weight_g * instance.quantity, 2)
    instance.energy_kj = round(
        instance.portion.energy_kj * instance.quantity, 2)
    instance.protein_g = round(
        instance.portion.protein_g * instance.quantity, 2)
    instance.fat_g = round(instance.portion.fat_g * instance.quantity, 2)
    instance.saturated_fatty_acids_g = round(
        instance.portion.saturated_fatty_acids_g * instance.quantity, 2)
    instance.sugar_g = round(instance.portion.sugar_g * instance.quantity, 2)
    instance.sodium_mg = round(
        instance.portion.sodium_mg * instance.quantity, 2)
    instance.carbohydrate_g = round(
        instance.portion.carbohydrate_g * instance.quantity, 2)
    instance.fibre_g = round(instance.portion.fibre_g * instance.quantity, 2)

    instance.weight_recipe_factor = round(
        instance.weight_g / instance.recipe.weight_g, 3)
    instance.nutri_points = round(
        instance.portion.ingredient.nutri_points * instance.weight_recipe_factor, 1)
    instance.nutri_class = NutriClass.get_nutri_class(
        'solid', instance.portion.ingredient.nutri_points)


# pylint: disable=unused-argument
@receiver(pre_save, sender=Ingredient)
def save_recipe(sender, instance: Ingredient, **kwargs):
    print('pre_save')
    import requests
    import json
    if instance.fdc_id:
        API_URL = "https://api.nal.usda.gov/fdc/v1/food"
        API_KEY = "?api_key=wrSx9QbtEeaZb3LHWXzm4egDf2uiBPdOEmGsc9tT"

        response = requests.get(f"{API_URL}/{instance.fdc_id}/{API_KEY}")
        dict_data = json.loads(response.text)
        if 'foodNutrients' in dict_data:
            nutri_list = dict_data['foodNutrients']
            instance.energy_kj = 0
            instance.protein_g = 0
            instance.saturated_fatty_acids_g = 0
            instance.fat_g = 0
            instance.sugar_g = 0
            instance.sodium_mg = 0
            instance.carbohydrate_g = 0
            instance.fibre_g = 0
            if 'ndbNumber' in dict_data:
                instance.ndb_number = dict_data['ndbNumber']

            if 'foodCategory' in dict_data:
                instance.major_class = dict_data['foodCategory']['description']

            for item in nutri_list:
                if item['type'] == 'FoodNutrient':
                    nutrient = item['nutrient']

                    if (nutrient['id'] == 2047):
                        instance.energy_kj = round(
                            int(item['amount']) * 4.1, 0)
                    elif (nutrient['id'] == 1008):
                        instance.energy_kj = round(
                            int(item['amount']) * 4.1, 0)

                    if (nutrient['id'] == 1003):
                        instance.protein_g = item['amount']

                    if (nutrient['id'] == 1258):
                        instance.saturated_fatty_acids_g = item['amount']

                    if (nutrient['id'] == 2000):
                        instance.sugar_g = item['amount']

                    if (nutrient['id'] == 1004):
                        instance.fat_g = item['amount']

                    if (nutrient['id'] == 1093):
                        instance.sodium_mg = item['amount']
                        instance.sodium_mg = item['amount']

                    if (nutrient['id'] == 1005):
                        instance.carbohydrate_g = item['amount']

                    if (nutrient['id'] == 1079):
                        instance.fibre_g = item['amount']

# pylint: disable=unused-argument


@receiver(post_save, sender=Ingredient)
def post_save_recipe(sender, instance, created, **kwargs):
    if not getattr(instance, 'processed', False):
        NutriClass = Nutri()
        physical_viscosity = instance.physical_viscosity
        nutri_items = NutriClass.get_nutri_items()
        nutri_points = 0
        for item in nutri_items:
            print(item)
            value = instance._meta.get_field(item).value_from_object(instance)
            print(value)
            temp_points = NutriClass.get_points(
                item, physical_viscosity, value)
            nutri_points = temp_points + nutri_points

        instance.nutri_points = nutri_points
        instance.nutri_class = NutriClass.get_nutri_class(
            'solid', instance.nutri_points)
        instance.processed = True
        instance.save()

        if created:
            Portion.objects.create(ingredient=instance,
                                   name=f'{instance.name} in g')
