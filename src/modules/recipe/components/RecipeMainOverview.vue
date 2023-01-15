<template>
  <div>
    <RecipeItemList
      @openRecipeItemAdd="openRecipeItemAdd"
      @openRecipeItemUpdate="openRecipeItemUpdate"
      :recipeItems="recipeItems"
      :editable="isEditable"
    />
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
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
