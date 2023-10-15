<template>
  <TabWrapper>
    <SimpleList
      :items="eventFiltered"
      :isLoading="isLoading"
      detailPageLink="EventDefault"
    >
      <template v-slot:notEmpty="slotProps">
        <MealListItem :item="slotProps.item" />
      </template>
      <template v-slot:empty>
        <h1>Leer</h1>
      </template>
    </SimpleList>
  </TabWrapper>
</template>
  
<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import SimpleList from "@/components/list/SimpleList.vue";
import TabWrapper from "@/components/base/TabWrapper.vue";
import MealListItem from "@/modules/meal/components/MealListItem.vue";

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const events = ref([]);
const isLoading = ref(false);

const eventFiltered = computed(() => {
  return events.value;
});

async function loadData() {
  isLoading.value = true;
  const response = await mealStore.fetchPublicEventsSmall();
  events.value = response.data;
  isLoading.value = false;
}

onMounted(async () => {
  await loadData();
});
</script>
