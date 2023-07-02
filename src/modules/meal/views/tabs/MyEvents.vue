<template>
  <TabWrapper>
    <!-- Tabs -->
    <div class="sm:hidden">
      <label for="tabs" class="sr-only">Select a tab</label>
      <select
        id="tabs"
        name="tabs"
        @change="onChange($event)"
        v-model="selectedValue"
        class="mt-4 block w-full rounded-md border-gray-300 py-2 pl-3 pr-10 text-base focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
      >
        <option
          :value="tab.name"
          v-for="tab in tabs"
          :key="tab.name"
          :selected="selectedValue"
        >
          {{ tab.name }} ({{ tab.count }})
        </option>
      </select>
    </div>
    <div class="hidden sm:block">
      <PrimaryButton @click="onEventAddClicked">Neues Event</PrimaryButton>
      <div class="border-b border-gray-200">
        <nav class="mt-2 -mb-px flex space-x-8" aria-label="Tabs">
          <router-link
            v-for="tab in tabs"
            :key="tab.name"
            :to="tab.linkName"
            :class="[
              tab.current
                ? 'border-blue-500 text-blue-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-200',
              'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm',
            ]"
          >
            {{ tab.name }}
            <span
              v-if="tab.count"
              :class="[
                tab.current
                  ? 'bg-blue-100 text-blue-600'
                  : 'bg-gray-100 text-gray-900',
                'hidden ml-2 py-0.5 px-2.5 rounded-full text-xs font-medium md:inline-block',
              ]"
              >{{ tab.count }}</span
            >
          </router-link>
        </nav>
      </div>
    </div>
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
    <EventAddEdit
      :open="openEventAddEdit"
      @close="onEventAddEditClose"
      header="Veranstaltung"
    />
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
import EventAddEdit from "@/modules/meal/components/EventAddEdit/EventAddEdit.vue";
import PrimaryButton from "@/components/button/Primary.vue";

const router = useRouter();

import { useRecipeStore } from "@/modules/recipe/store/index";
const recipeStore = useRecipeStore();

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const isLoading = computed(() => {
  return mealStore.isLoading;
});

const events = computed(() => {
  return mealStore.events;
});

const eventFiltered = computed(() => {
  const query = { ...router.currentRoute.value.query };
  return events.value;
});

const selectedValue = ref("Aktive Anmeldephase");
const openEventAddEdit = ref(false);


function onChange(event) {
  const linkName = tabs.value.find((item) => item.name === selectedValue.value)[
    "linkName"
  ];
  router.push(linkName);
}

watch(() => router.currentRoute.value.query, refresh);

const tabs = computed(() => {
  const query = { ...router.currentRoute.value.query };

  return [
  ];
});

function refresh() {
  mealStore.fetchEventsSmall();
}

function onEventAddClicked() {
  openEventAddEdit.value = true;
}

function onEventAddEditClose() {
  openEventAddEdit.value = false;
}

onMounted(() => {
  refresh();
});
</script>

