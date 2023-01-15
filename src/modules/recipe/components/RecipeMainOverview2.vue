<template>
  <div>
    <div v-for="item in items" :key="item.id">
      <RecipeOverviewItem :item="item" :recipeDetail="recipeDetail" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
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

const items = [
  {
    id: 1,
    name: "Energie",
    value: "energyKj",
    unit: "kJ",
  },
  {
    id: 2,
    name: "Zucker",
    value: "sugarG",
    unit: "g",
  },
  {
    id: 3,
    name: "gesä. Fett",
    value: "fatSatG",
    unit: "g",
  },
  {
    id: 4,
    name: "Natrium",
    value: "sodiumMg",
    unit: "mg",
  },
  {
    id: 5,
    name: "Eiweiß",
    value: "proteinG",
    unit: "g",
  },
  {
    id: 6,
    name: "Ballaststoffe",
    value: "fibreG",
    unit: "g",
  },
];

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
