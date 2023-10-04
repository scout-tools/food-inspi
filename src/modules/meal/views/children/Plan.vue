<template>
  <div>
    <h1>Hallo</h1>
  </div>
</template>
  
  
  <script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";

import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

const route = useRoute();

const mealStore = useMealStore();


onMounted(() => {
  const id = route.params.id;
});
</script>
  