<template>
  <div>
    <div v-if="!isLoading">
      <fieldset class="">
        <legend class="sr-only">Notifications</legend>
        <nav class="h-full overflow-y-auto" aria-label="shoppingList">
          <div
            v-for="letter in Object.keys(shoppingList)"
            :key="letter"
            class="relative"
          >
            <div
              class="sticky top-0 z-10 border-t border-b border-gray-200 bg-gray-50 px-6 py-1 text-sm font-medium text-gray-500"
            >
              <h3>{{ letter }}</h3>
            </div>
            <ul role="list" class="relative z-0 divide-y divide-gray-200">
              <li
                v-for="item in Object.keys(shoppingList[letter])"
                :key="item"
                class="bg-white"
              >
                <div
                  class="relative flex items-center space-x-3 px-6 py-5 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 hover:bg-gray-50"
                >
                  <div class="min-w-0 flex-1">
                    <!-- Extend touch target to entire panel -->
                    <span class="absolute inset-0" aria-hidden="true" />
                    <p class="text-sm font-medium text-gray-900">
                      {{ item }} (aus
                      {{ shoppingList[letter][item][0].recipeName }})
                    </p>
                    <p class="truncate text-sm text-gray-500">
                      {{ shoppingList[letter][item][0].weightShow }} -
                      {{ shoppingList[letter][item][0].price.toFixed(2) }} €
                    </p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </nav>
        <div v-if="shoppingList && !Object.keys(shoppingList).length">
          <LoadingItem />
        </div>
      </fieldset>
    </div>
    <div v-else>
      <LoadingItem />
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";

import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

const route = useRoute();

const shoppingList = computed(() => {
  return mealStore.shoppingList;
});

const mealStore = useMealStore();

const isLoading = computed(() => {
  return !mealStore.shoppingList;
});

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchShoppingList({ id });
});
</script>
