from django.db.models import Q, QuerySet
from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from food import models as food_models
from food import serializers as food_serializers


class MeasuringUnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.MeasuringUnit.objects.all()
    serializer_class = food_serializers.MeasuringUnitSerializer


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Price.objects.all()
    serializer_class = food_serializers.PriceSerializer


class TagCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.TagCategory.objects.all()
    serializer_class = food_serializers.TagCategorySerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Tag.objects.all()
    serializer_class = food_serializers.TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = food_models.Ingredient.objects.all()
    serializer_class = food_serializers.IngredientSerializer


class RecipeItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.RecipeItem.objects.all()
    serializer_class = food_serializers.RecipeItemSerializer


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Recipe.objects.all()
    serializer_class = food_serializers.RecipeSerializer


class RetailerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Retailer.objects.all()
    serializer_class = food_serializers.RetailerSerializer


class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Package.objects.all()
    serializer_class = food_serializers.PackageSerializer


class PortionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = food_models.Portion.objects.all()
    serializer_class = food_serializers.PortionSerializer
