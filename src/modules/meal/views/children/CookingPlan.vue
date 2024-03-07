<template>
  <div class="flex h-full flex-col">
    <div v-for="item in mealItems" :key="item.id">
      <CookingPlanItem :item="item" class="my-3"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

import CookingPlanItem from "@/modules/meal/components/cookingPlan/Item.vue";

const mealStore = useMealStore();

const route = useRoute();

const mealItems = ref([]);

onMounted(async () => {
  const eventId = route.params.id;
  const response = await mealStore.fetchMealCookingPlan({ eventId: eventId });
  if (response?.data) {
    mealItems.value = response?.data;
  }
});
</script>
  