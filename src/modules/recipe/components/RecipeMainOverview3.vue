<template>
  <div class="mx-auto max-w-7xl sm:px-2 lg:px-8 mt-16">
    <div class="mx-auto max-w-2xl space-y-8 sm:px-4 lg:max-w-4xl lg:px-0">
      <div
        class="
          border-t border-b border-gray-200
          bg-gray-50
          px-4
          py-6
          shadow
          sm:rounded-lg sm:border
        "
      >
        <PriceList
          :recipeItems="recipeItems"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import PriceList from "@/modules/recipe/components/PriceList.vue";
import NutritionalsBoxPlot from "@//modules/recipe/components/chart/NutritionalsBoxPlot.vue";
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
