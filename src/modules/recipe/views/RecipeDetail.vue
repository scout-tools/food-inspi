<template>
  <div class="2xl:px-64 xl:px-30">
    <main class="relative z-0 flex-1 overflow-y-auto focus:outline-none">
      <!-- Breadcrumb -->
      <Breadcrumbs :pages="pages" />
      <article>
        <RecipeOverview 
          :recipeItems="recipeDetail.recipeItems"/>
      </article>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

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

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
