<template>
  <div class="flex h-full flex-col">
    <div v-for="item in mealItems" :key="item.id">
      <PlanItem :item="item" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import {
  ChevronDownIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  EllipsisHorizontalIcon,
} from "@heroicons/vue/20/solid";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

import PlanItem from "@/modules/meal/components/plan/Item.vue";

const mealStore = useMealStore();

const route = useRoute();

const event = computed(() => {
  return mealStore.mealEvent;
});

const eventDays = computed(() => {
  let days = [];
  mealStore?.mealEvent?.mealDays.forEach((day) => {
    days.push(day.date);
  });
  return days;
});

function range(start, end) {
  return Array(end - start + 1)
    .fill()
    .map((_, idx) => start + idx);
}

const dayHours = computed(() => {
  return range(7, 22);
});

const mealItems = computed(() => {
  let mealItems = [];
  let id = 1;
  mealStore?.mealEvent?.mealDays.forEach((day: object, dayIndex: int) => {
    day.meals.forEach((meal: object) => {
      const startDate = parseInt(meal.timeStart?.split(":")[0], 10);
      const endDate = parseInt(meal.timeEnd?.split(":")[0], 10);
      mealItems.push({
        id,
        name: meal.name,
        start: startDate,
        end: endDate,
        dayIndex: eventDays?.value?.indexOf(meal?.mealDay?.date) + 1,
        day: day,
        priceEur: meal.priceEur,
        getMealTypeDisplay: meal.getMealTypeDisplay,
        mealItems: meal.mealItems,
      });
      id = id + 1;
    });
  });
  return mealItems;
});
</script>
  