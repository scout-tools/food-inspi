<template>
  <div class="lg:border-t lg:border-b lg:border-gray-200"></div>
</template>


<script setup lang="ts">
import { onMounted } from "vue";
import { useRecipeStore } from "@/modules/recipe/store";
import { useRouter } from "vue-router";

const router = useRouter();

const recipeStore = useRecipeStore();

onMounted(() => {
  debugger;
  recipeStore.createRecipe({}).then((response) => {
    debugger;
    router.push({
      name: "SimulatorMain",
      params: { id: response?.data.id },
    });
  });
});
</script>