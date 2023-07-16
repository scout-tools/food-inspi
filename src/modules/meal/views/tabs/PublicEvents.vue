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
import { ref, watch, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import {
  ScaleIcon,
  UserGroupIcon,
  UserIcon,
  BellIcon,
} from "@heroicons/vue/24/outline";
import { useTaskStore } from "@/modules/task/store/index";
import { useDashboardStore } from "@/modules/dashboard/store/index";
import RequestListButton from "@/modules/group/components/RequestListButton.vue";
import SimpleList from "@/components/list/SimpleList.vue";
import TabWrapper from "@/components/base/TabWrapper.vue";
import RecipeListItem from "@/modules/recipe/components/RecipeListItem.vue";
import MealListItem from "@/modules/meal/components/MealListItem.vue";
import EventListItemEmpty from "@/modules/event/components/EventListItemEmpty.vue";
import { useEventStore } from "@/modules/event/store";

const router = useRouter();

import { useRecipeStore } from "@/modules/recipe/store/index";
const recipeStore = useRecipeStore();

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const isLoading = computed(() => {
  return mealStore.isLoading;
});

const events = computed(() => {
  return mealStore.mealEvents;
});

const eventFiltered = computed(() => {
  return events.value;
});

const selectedValue = ref("Aktive Anmeldephase");

function onChange(event) {
  const linkName = tabs.value.find((item) => item.name === selectedValue.value)[
    "linkName"
  ];
  router.push(linkName);
}

const tabs = computed(() => {
  const query = { ...router.currentRoute.value.query };

  return [
    {
      name: "Warm",
      linkName: { name: "RecipeApproved", query: { meal_type: "lunch_warm" } },
      count: events.value.filter((q) => q.mealType === "lunch_warm").length,
      current: query.meal_type === "lunch_warm",
    },
  ];
});

function refresh() {
  mealStore.fetchPublicEvents();
}

onMounted(() => {
  refresh();
});
</script>
