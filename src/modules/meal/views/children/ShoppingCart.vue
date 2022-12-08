<template>
  <fieldset class="space-y-5">
    <legend class="sr-only">Notifications</legend>
    <div class="relative flex items-start" v-for="item in shoppingList" :key="item.name">
      <div class="flex h-5 items-center">
        <input
          id="comments"
          aria-describedby="comments-description"
          name="comments"
          type="checkbox"
          class="
            mt-4
            h-8
            w-8
            rounded
            border-gray-300
            text-blue-600
            focus:ring-indigo-500
          "
        />
      </div>
      <div class="ml-3 text-lg">
        <label for="comments" class="font-medium text-gray-700"> {{ item.ingredientName}} ({{ item.ingredientClass}})</label>
        <p id="comments-description" class="text-gray-500">
          {{ getWeightString(item)}} aus {{ item.recipeName}}
        </p>
      </div>
    </div>
    <div v-if="shoppingList && !shoppingList.length">
      <h2> Keine Rezepte ausgewählt </h2>
    </div>
  </fieldset>
</template>


<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";

import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

const route = useRoute();

const shoppingList = computed(() => {
  return mealStore.shoppingList;
});

function getWeightString(item) {
  if (item.weightG < 1000) {
    return `${item.weightG} g`
  }
  return `${item.weight_Kg} Kg`
}

const mealStore = useMealStore();

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchShoppingList({id});
});
</script>
