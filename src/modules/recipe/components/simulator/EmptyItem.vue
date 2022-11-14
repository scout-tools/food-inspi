<template>
  <div class="text-center my-12">
    <div class="object-center sm:hidden">
      <router-link :to="{ name: 'SimulatorStart' }">
        <img
          class="h-40 mx-auto object-center w-auto"
          src="./../../../../assets/logo.png"
          alt="Food Inspi"
        />
      </router-link>
    </div>
    <svg
      class="mx-auto invisible sm:visible h-12 w-12 text-gray-400"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
      aria-hidden="true"
    >
      <path
        vector-effect="non-scaling-stroke"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
      />
    </svg>
    <h3 class="mt-2 text-sm font-medium text-gray-900">
      Lass deine Rezept von mir bewerten.
    </h3>
    <p class="mt-1 text-sm text-gray-500">
      Füge jetzt deine Zutaten ein. Ich habe sicher einen Tipp für dich.
    </p>
    <div class="mt-6 mb-6">
      <button
        type="button"
        @click="onAddRecipeItem"
        class="
          inline-flex
          items-center
          rounded-md
          border border-transparent
          bg-blue-600
          px-4
          py-2
          text-sm
          font-medium
          text-white
          shadow-sm
          hover:bg-blue-700
          focus:outline-none
          focus:ring-2
          focus:ring-blue-500
          focus:ring-offset-2
        "
      >
        <PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
        Neues Rezept
      </button>
    </div>
    <div class="mt-8 flex flex-col">
      <div class="my-2 mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div
            class="
              overflow-hidden
              shadow
              ring-1 ring-black ring-opacity-5
              md:rounded-lg
            "
          >
            <table class="min-w-full divide-y divide-gray-300">
              <thead class="bg-gray-50">
                <tr>
                  <th
                    scope="col"
                    class="
                      py-3.5
                      pl-4
                      pr-3
                      text-left text-sm text-gray-900
                      sm:pl-6
                    "
                  >
                    Bestehende Rezepte
                  </th>
                  <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                    <span class="sr-only"></span>
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="recipe in recipes" :key="recipe.id">
                  <td
                    class="
                      whitespace-nowrap
                      py-4
                      pl-4
                      pr-3
                      text-left text-sm
                      font-medium
                      text-gray-900
                      sm:pl-6
                    "
                  >
                    {{ recipe.name }}
                  </td>
                  <td
                    class="
                      relative
                      whitespace-nowrap
                      py-4
                      pl-3
                      pr-4
                      text-right text-sm
                      font-medium
                      sm:pr-6
                    "
                  >
                    <button
                      @click="onSimulateClicked(recipe.id)"
                      class="text-indigo-600 hover:text-indigo-900"
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
import { useRecipeStore } from "@/modules/recipe/store/index.ts";
import { useRouter } from "vue-router";

const router = useRouter();

const recipeStore = useRecipeStore();

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

onMounted(() => {
  recipeStore.fetchRecipes();
});
</script>
