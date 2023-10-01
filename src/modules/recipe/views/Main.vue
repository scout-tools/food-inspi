<template>
  <div class="2xl:px-64 xl:px-30">
    <List
      :name="'Rezepte'"
      :items="recipes"
      :searchValue="searchValue"
      :sortOptions="sortOptions"
      :filters="filters"
      :buttonList="buttonList"
      mainPageLink="RecipesMain"
      detailPageLink="RecipeDetail"
      :isLoading="isLoading"
    >
      <template #listitem="{ item }">
        <div class="flex min-w-0 flex-1 items-center">
          <div class="min-w-0 flex-1 px-4 md:grid md:grid-cols-2 md:gap-4">
            <div>
              <p class="truncate text-sm font-medium text-blue-600">
                {{ item.name }}
              </p>
              <p class="truncate text-sm font-medium text-gray-500">
                {{ item.priceEur.toFixed(2) }} €
              </p>
              <p class="mt-2 flex items-center text-sm text-gray-500">
                <TagIcon
                  class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
                  aria-hidden="true"
                />
                <span class="truncate">{{ item.getMealTypeDisplay }}</span>
              </p>
            </div>
            <div class="hidden md:block">
              <div>
                <p class="mt-1 flex items-center text-sm text-gray-500">
                  <NutriSlim :nutriClass="item.nutriClass" />
                </p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </List>
  </div>
</template>

<script setup lang="ts">
import List from "@/components/base/list/Main.vue";

import { TagIcon } from "@heroicons/vue/20/solid";

import { onMounted, computed, watch, ref } from "vue";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

const recipeStore = useRecipeStore();
const recipes = computed(() => {
  return recipeStore.recipes;
});

const isLoading = computed(() => {
  return !recipeStore.recipes && recipeStore.isLoading && recipeStore.recipes.length === 0;
});


const route = useRoute();

watch(
  () => route.query,
  () => {
    updateSearch(route.query);
  },
  { immediate: true, deep: true }
);

function updateSearch(params) {
  recipeStore.fetchRecipes(params);
}

onMounted(() => {
  recipeStore.fetchRecipes(route.query);
});

const sortOptions = [
  { name: "A-Z", value: "alpha", current: true },
  { name: "Neuste", value: "-created_at", current: false },
  { name: "Gesund", value: "nutri_points", current: false },
];

const filters = [
  {
    id: "nutri_class",
    name: "Nutri Score",
    options: [
      { value: "1", label: "Klasse A", checked: false },
      { value: "2", label: "Klasse B", checked: false },
      { value: "3", label: "Klasse C", checked: false },
      { value: "4", label: "Klasse D", checked: false },
      { value: "5", label: "Klasse E", checked: false },
    ],
  },
  {
    id: "status",
    name: "Status",
    options: [
      { value: "verified", label: 'Verified by Inspi', checked: false },
      { value: "user_conent", label: 'Benutzer erstellt', checked: false },
      { value: "user_public", label: 'Benutzer Öffentlich', checked: false },
    ],
  },
  {
    id: "meal_type", 
    name: "Mahlzeit Typ",
    options: [
      { value: "breakfast", label: 'Frühstück', checked: false },
      { value: "lunch_warm", label: 'Menu (warm)', checked: false },
      { value: "lunch_cold", label: 'Menu (kalt)', checked: false },
      { value: "snack", label: 'Snack', checked: false },
    ],
  },
];
const buttonList = [{ name: "Neues Rezept", linkName: "RecipeCreate" }];

const searchValue = ref();
</script>