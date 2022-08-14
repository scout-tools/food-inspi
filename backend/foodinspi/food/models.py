from django.db import models
from django.db.models import Sum

from food.service.nutri_lib import Nutri


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
    tag_category = models.ForeignKey(TagCategory, on_delete=models.PROTECT, null=True)
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
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    fdc_id = models.IntegerField(null=True, blank=True)
    # readonly
    nutri_points = models.IntegerField(null=True, blank=True)
    nutri_class = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        NutriClass = Nutri()
        physical_viscosity = self.physical_viscosity
        nutri_items = NutriClass.get_nutri_items()
        nutri_points = 0
        for item in nutri_items:
            value = self._meta.get_field(item).value_from_object(self)
            temp_points = NutriClass.get_points(item, physical_viscosity, value)
            nutri_points = temp_points + nutri_points

        self.nutri_points = nutri_points
        self.nutri_class = NutriClass.get_nutri_class('soild', self.nutri_points)
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Portion(TimeStampMixin, NutrientsMixin):
    name = models.CharField(max_length=255, blank=True)
    measuring_unit = models.ForeignKey(MeasuringUnit, on_delete=models.PROTECT, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.FloatField()
    rank = models.IntegerField(default=1)
    # readonly
    weight_g = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        is_g = self.measuring_unit.unit == 'g'
        if is_g:
            self.weight_g = self.measuring_unit.quantity * self.quantity
        else:
            self.weight_g = self.measuring_unit.quantity * self.quantity * self.ingredient.physical_density
        
        # Nutrients
        self.energy_kj = round(self.ingredient.energy_kj * self.weight_g / 100, 2)
        self.protein_g = round(self.ingredient.protein_g * self.weight_g / 100, 2)
        self.fat_g = round(self.ingredient.fat_g * self.weight_g / 100, 2)
        self.saturated_fatty_acids_g = round(self.ingredient.saturated_fatty_acids_g * self.weight_g / 100, 2)
        self.sugar_g = round(self.ingredient.sugar_g * self.weight_g / 100, 2)
        self.sodium_mg = round(self.ingredient.sodium_mg * self.weight_g / 100, 2)
        self.carbohydrate_g = round(self.ingredient.carbohydrate_g * self.weight_g / 100, 2)
        self.fibre_g = round(self.ingredient.fibre_g * self.weight_g / 100, 2)
        
        super(Portion, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} / {self.quantity} {self.measuring_unit}'

    def __repr__(self):
        return self.__str__()

class Recipe(TimeStampMixin, NutrientsMixin):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    
    # readonly
    nutri_class = models.FloatField(null=True, blank=True)
    nutri_points = models.FloatField(null=True, blank=True)
    weight_g = models.FloatField(default=1)

    def get_sum(self, name, items):
        if (items[f'{name}__sum']):
            return round(items[f'{name}__sum'], 0)
        return 0


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

        self.weight_g =  self.get_sum('weight_g', items)
        self.nutri_points = self.get_sum('nutri_points', items)
        self.nutri_class = NutriClass.get_nutri_class('solid', self.nutri_points)
        self.energy_kj = self.get_sum('energy_kj', items)
        self.protein_g = self.get_sum('protein_g', items)
        self.fat_g = self.get_sum('fat_g', items)
        self.saturated_fatty_acids_g = self.get_sum('saturated_fatty_acids_g', items)
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
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, blank=True, null=True)
    portion = models.ForeignKey(Portion, on_delete=models.PROTECT)
    quantity = models.FloatField(default=1)
    # readonly
    weight_g = models.FloatField(blank=True, null=True)
    weight_recipe_factor = models.FloatField(blank=True, null=True)
    nutri_points = models.FloatField(blank=True, null=True)
    nutri_class = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        NutriClass = Nutri()
        self.weight_g = round(self.portion.weight_g * self.quantity, 2)
        self.energy_kj = round(self.portion.energy_kj * self.quantity, 2)
        self.protein_g = round(self.portion.protein_g * self.quantity, 2)
        self.fat_g = round(self.portion.fat_g * self.quantity, 2)
        self.saturated_fatty_acids_g = round(self.portion.saturated_fatty_acids_g * self.quantity, 2)
        self.sugar_g = round(self.portion.sugar_g * self.quantity, 2)
        self.sodium_mg = round(self.portion.sodium_mg * self.quantity, 2)
        self.carbohydrate_g = round(self.portion.carbohydrate_g * self.quantity, 2)
        self.fibre_g = round(self.portion.fibre_g * self.quantity, 2)

        if (self.recipe.weight_g == 0):
            self.recipe.weight_g = 1

        self.weight_recipe_factor = round(self.weight_g / self.recipe.weight_g, 3)
        self.nutri_points = round(self.portion.ingredient.nutri_points * self.weight_recipe_factor, 1)
        self.nutri_class =  NutriClass.get_nutri_class('solid', self.portion.ingredient.nutri_points)
        super(RecipeItem, self).save(*args, **kwargs)

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
    name = models.CharField(max_length=255, blank=True)
    quantity = models.FloatField(default=1)
    portion = models.ForeignKey(Portion, on_delete=models.PROTECT, null=True)
    # readonly
    weight_package_g = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.weight_package_g = 1
        super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}  / {self.weight_package_g} g'

    def __repr__(self):
        return self.__str__()


class Price(TimeStampMixin):
    price_eur = models.FloatField()
    retailer = models.ForeignKey(Retailer, on_delete=models.PROTECT, blank=True)
    package = models.ForeignKey(Package, on_delete=models.PROTECT, null=True)

    #readonly
    price_per_kg = models.FloatField(default=1)

    def save(self, *args, **kwargs):
        self.price_per_kg = 1
        super(Price, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.package} - {self.price_eur} € - {self.retailer}'

    def __repr__(self):
        return self.__str__()
