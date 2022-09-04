from rest_framework import serializers
from food import models as food_models
from django.contrib.auth.models import User

from food import serializers as food_serializers


class MeasuringUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.MeasuringUnit
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Price
        fields = '__all__'


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Hint
        fields = '__all__'


class TagCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.TagCategory
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Tag
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Ingredient
        fields = '__all__'


class RecipeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.RecipeItem
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    hints = food_serializers.HintSerializer(many=True)
    tags = food_serializers.TagSerializer(many=True)

    class Meta:
        model = food_models.Recipe
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Retailer
        fields = '__all__'


class PortionSerializer(serializers.ModelSerializer):
    ingredient = food_serializers.IngredientSerializer()
    measuring_unit = food_serializers.MeasuringUnitSerializer()
    class Meta:
        model = food_models.Portion
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.Package
        fields = '__all__'
