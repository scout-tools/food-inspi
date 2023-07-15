<template>
  <div class="2xl:px-64 xl:px-30">
    <div class="text-center">
      <h2 class="mt-2 text-lg font-medium text-gray-900">Simulator</h2>
    </div>
    <RecipeOverview
      :recipeItems="recipeDetail.recipeItems"
      @openRecipeItemUpdate="onOpenRecipeItemUpdate"
      @openRecipeItemAdd="openRecipeItemAdd"
      isEditable="true"
    />

    <RecipeOverviewNutri
      :recipeItems="recipeDetail.recipeItems"
      @openRecipeItemUpdate="onOpenRecipeItemUpdate"
      @openRecipeItemAdd="openRecipeItemAdd"
      isEditable="true"
    />
    <RecipeOverview2
      :recipeItems="recipeDetail.recipeItems"
      @openRecipeItemUpdate="onOpenRecipeItemUpdate"
      @openRecipeItemAdd="openRecipeItemAdd"
      isEditable="true"
    />
    <RecipeOverview3
      :recipeItems="recipeDetail.recipeItems"
      @openRecipeItemUpdate="onOpenRecipeItemUpdate"
      @openRecipeItemAdd="openRecipeItemAdd"
      isEditable="true"
    />
    <RecipeItemUpdate
      :open="openRecipeItemUpdate"
      :reciptItem="openRecipeItem"
      @close="onRecipeItemUpdateClose"
      header="Zutat"
    />
    <div
      class="
        px-2
        py-2
        sm:flex sm:items-center sm:justify-between sm:px-6
        lg:px-8
      "
    >
      <div class="min-w-0 flex-1"></div>
      <div class="mt-4 flex-2 sm:mt-0 sm:ml-4">
        <PrimaryButton
          color="blue"
          label="Rezept speichern"
          @click="onAddRecipe(recipeDetail)"
        />
      </div>
    </div>
    <CreateRecipe
      :open="openRecipeUpdate"
      @close="onRecipeUpdateClose"
      :items="recipeDetail"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import PrimaryButton from "@/components/button/Primary.vue";
import EmptyItem from "@/modules/recipe/components/simulator/EmptyItem.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import RecipeOverview2 from "@/modules/recipe/components/RecipeMainOverview2.vue";
import RecipeOverview3 from "@/modules/recipe/components/RecipeMainOverview3.vue";
import RecipeOverviewNutri from "@/modules/recipe/components/RecipeMainOverviewNutri.vue";
import RecipeItemUpdate from "@/modules/recipe/components/RecipeItem/RecipeItem.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index";

import CreateRecipe from '@/modules/recipe/components/simulator/createRecipe/CreateRecipe.vue'

const route = useRoute();

const openRecipeItemUpdate = ref(false);
const openRecipeItem = ref({});

const recipeStore = useRecipeStore();

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

function openRecipeItemAdd() {
  openRecipeItem.value = {};
  openRecipeItemUpdate.value = true;
}

function onOpenRecipeItemUpdate(reciptItem: Object) {
  openRecipeItemUpdate.value = true;
  openRecipeItem.value = reciptItem;
}

function onRecipeItemUpdateClose() {
  openRecipeItemUpdate.value = false;
}

const openRecipeUpdate = ref(false);


function onRecipeUpdateClose() {
  openRecipeUpdate.value = false;
}

function onAddRecipe(reciptItem: Object) {
  openRecipeUpdate.value = true;
  openRecipeItem.value = reciptItem;
}

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
