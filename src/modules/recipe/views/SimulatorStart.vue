<template>
  <PageWrapper>
    <MyTabGroup :tabs="tabs" />
  </PageWrapper>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";

import MyTabGroup from "@/components/menu/TabGroup.vue";
import PageWrapper from "@/components/base/PageWrapper.vue";

const route = useRoute();

const tabs = computed(() => {
  return [
    {
      name: "Inspi's Rezepte",
      linkName: { name: "RecipeApproved", query: { meal_type: 'lunch_warm'} },
      current: route.name === "RecipeApproved",
    },
    {
      name: "Öffenliche Rezepte",
      linkName: { name: "RecipeUserPublic", query: { meal_type: 'lunch_warm'}  },
      current:
        route.name === "RecipeUserPublic"
    },
    {
      name: "Meine Rezepte",
      linkName: { name: "RecipeMyRecipes", query: { meal_type: 'lunch_warm'}},
      current: route.name === "RecipeMyRecipes",
    },
  ];
});
</script>
