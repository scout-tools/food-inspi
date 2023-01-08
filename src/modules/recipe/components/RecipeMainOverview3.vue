<template>
  <div>
    <div>
      <PriceList
        label="Engergie"
        :value="recipeDetail.energyKj"
        unit="kJ"
        :recipeItems="recipeItems"
      />
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
