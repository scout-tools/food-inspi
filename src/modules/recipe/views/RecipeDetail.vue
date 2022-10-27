<template>
  <div class="2xl:px-64">
    
    <main class="relative z-0 flex-1 overflow-y-auto focus:outline-none">
      <!-- Breadcrumb -->
      <Breadcrumbs :pages="pages"/>
      <article>
        <div class="overflow-auto bg-white shadow sm:rounded-lg">
          <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
            <dl class="sm:divide-y sm:divide-gray-200">
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">
                  Nutri
                </dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  <NutriBar :nutriClass="recipesDetail.nutriClass"/>
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">
                  Hinweise
                </dt>
                <dd v-if="recipesDetail && recipesDetail.hints && recipesDetail.hints.length" class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  <span v-for="hint in recipesDetail.hints" :key="hint.name" class="inline-flex rounded-full bg-red-100 px-2 text-xs font-semibold leading-5 text-red-800">{{ hint.name }}</span>
                </dd>
                <dd v-else class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  <span class="inline-flex rounded-full bg-green-100 px-2 text-xs font-semibold leading-5 text-green-800">Rezept ist super</span>
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">Zutaten</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  <ul
                    role="list"
                    class="
                      divide-y divide-gray-200
                      rounded-md
                      border border-gray-200
                    "
                  >
                    <li
                      v-for="item in recipesDetail.recipeItems" :key="item.name"
                      class="
                        flex
                        items-center
                        justify-between
                        py-3
                        pl-3
                        pr-4
                        text-sm
                      "
                    >
                      <div class="flex w-0 flex-1 items-center">
                        <ArchiveBoxIcon
                          class="h-5 w-5 flex-shrink-0 text-gray-400"
                          aria-hidden="true"
                        />
                        <span class="ml-2 w-0 flex-1 truncate"
                          >{{ item.quantity }} x {{ item.portion.name }} / {{ item.quantity * item.portion.weightG }} g</span
                        >
                      </div>
                    </li>
                  </ul>
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </article>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import {
  ArchiveBoxIcon,
} from "@heroicons/vue/24/outline";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue"
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

const route = useRoute();

const pages = computed(() => {
  return [
  { name: 'Rezepte', link: 'RecipesMain', current: false },
  { name: `${recipesDetail.value.name}`, link: `RecipeDetail`, current: true },
]
});

const recipeStore = useRecipeStore();
const recipesDetail = computed(() => {
  return recipeStore.recipesDetail;
});

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
