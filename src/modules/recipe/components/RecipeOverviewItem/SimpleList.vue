<template>
  <div class="text-center my-6">
    <div class="mt-8 flex flex-col">
      <div class="my-2 mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div>
      <label
        for="location"
        class="block text-sm font-medium leading-6 text-gray-900"
        >Mahlzeitart</label
      >
      <select
        id="location"
        name="location"
        class="mt-2 block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm sm:leading-6"
      >
        <option>United States</option>
        <option>Canada</option>
        <option>Mexico</option>
      </select>
    </div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">

          <div
            class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg"
          >
            <table class="min-w-full divide-y divide-gray-300">
              <thead class="bg-gray-50">
                <tr>
                  <th
                    scope="col"
                    class="py-3.5 pl-4 pr-3 text-left text-sm text-gray-900 sm:pl-6"
                  >
                    Rezepte
                  </th>
                  <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                    <span class="sr-only"></span>
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="recipe in recipes" :key="recipe.id">
                  <td
                    class="whitespace-nowrap py-4 pl-4 pr-3 text-left text-sm font-medium text-gray-900 sm:pl-6"
                  >
                    {{ recipe.name }}
                  </td>
                  <td
                    class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6"
                  >
                    <button
                      @click="onSimulateClicked(recipe.id)"
                      class="text-blue-600 hover:text-blue-900"
                    >
                      Simulieren
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import { PlusIcon } from "@heroicons/vue/20/solid";
import { useRecipeStore } from "@/modules/recipe/store/index";
const recipeStore = useRecipeStore();

import { useRouter } from "vue-router";

const router = useRouter();

const recipes = computed(() => {
  return recipeStore.recipes;
});

const emit = defineEmits(["onAddRecipeItem"]);

const onAddRecipeItem = () => {
  emit("onAddRecipeItem");
};

async function onSimulateClicked(id) {
  const response = await recipeStore.cloneRecipe(id);
  if (response && response.status == 201) {
    router.push({
      name: "SimulatorMain",
      params: { id: response.data.id },
    });
  }
}

onMounted(() => {});
</script>
