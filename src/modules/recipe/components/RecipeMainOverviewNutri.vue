<template>
  <dl class="sm:divide-y sm:divide-gray-200 border-t border-gray-200 px-2">
    <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
      <dt class="text-sm font-medium text-gray-500">Gesamt Nutri</dt>
      <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
        <NutriBar :nutriClass="recipeDetail.nutriClass" />
      </dd>
    </div>
  </dl>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import PriceList from "@/modules/recipe/components/PriceList.vue";
import RecipeOverviewItem from "@/modules/recipe/components/RecipeOverviewItem/Main.vue";
import NutritionalsBoxPlot from "@/modules/recipe/components/chart/NutritionalsBoxPlot.vue";
import ListItem from "@/modules/recipe/components/ListItem.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

const route = useRoute();
const props = defineProps({
  recipeItems: { type: Array, required: true },
  isEditable: { type: Boolean, required: false, default: false },
});

const emit = defineEmits(["openRecipeItemUpdate", "openRecipeItemAdd"]);

const openRecipeItemUpdate = (reciptItem: Object) => {
  emit("openRecipeItemUpdate", reciptItem);
};
const openRecipeItemAdd = () => {
  emit("openRecipeItemAdd");
};

const recipeStore = useRecipeStore();

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
