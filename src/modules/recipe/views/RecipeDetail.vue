<template>
  <div class="2xl:px-64 xl:px-30">
    <main class="relative z-0 flex-1 overflow-y-auto focus:outline-none">
      <!-- Breadcrumb -->
      <Breadcrumbs :pages="pages" />
      <article>
        <RecipeOverview :recipeItems="recipeDetail.recipeItems" />
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
              label="Simulieren"
              @click="onSimulateClicked(recipeDetail.id)"
            />
          </div>
        </div>
      </article>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";
import { useRouter } from "vue-router";

const router = useRouter();

const route = useRoute();

const pages = computed(() => {
  return [
    { name: "Rezepte", link: "RecipesMain", current: false },
    { name: `${recipeDetail.value.name}`, link: `RecipeDetail`, current: true },
  ];
});

const recipeStore = useRecipeStore();

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

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
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
