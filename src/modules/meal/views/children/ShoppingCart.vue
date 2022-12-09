<template>
  <fieldset class="space-y-5">
    <legend class="sr-only">Notifications</legend>
    <nav class="h-full overflow-y-auto" aria-label="shoppingList">
      <div
        v-for="letter in Object.keys(shoppingList)"
        :key="letter"
        class="relative"
      >
        <div
          class="
            sticky
            top-0
            z-10
            border-t border-b border-gray-200
            bg-gray-50
            px-6
            py-1
            text-lg
            font-medium
            text-gray-500
          "
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
              class="
                relative
                flex
                items-center
                space-x-3
                px-6
                py-5
                focus-within:ring-2
                focus-within:ring-inset
                focus-within:ring-indigo-500
                hover:bg-gray-50
              "
            >
              <input
                id="comments"
                aria-describedby="comments-description"
                name="comments"
                type="checkbox"
                class="
                  mr-2
                  h-8
                  w-8
                  rounded
                  border-gray-300
                  text-blue-600
                  focus:ring-indigo-500
                "
              />
              <div class="min-w-0 flex-1">
                  <!-- Extend touch target to entire panel -->
                  <span class="absolute inset-0" aria-hidden="true" />
                  <p class="text-lg font-medium text-gray-900">
                    {{ item }} (aus {{ shoppingList[letter][item][0].recipeName }})
                  </p>
                  <p class="truncate text-lg text-gray-500">
                    {{ shoppingList[letter][item][0].weightShow }}
                  </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    <div v-if="shoppingList && !shoppingList.length">
      <h2>Keine Rezepte ausgewählt</h2>
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

const mealStore = useMealStore();

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchShoppingList({ id });
});
</script>
