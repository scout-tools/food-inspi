<template>
  <div>
    <div v-if="!isLoading">
      <Breadcrumbs :pages="pages" />
      <div
        v-if="!isShoppingRoute"
        class="mx-8 my-4 border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
      >
        <div class="pb-5">
          <h3 class="text-lg leading-6 text-gray-900">
            {{ props.event?.event?.name }}
          </h3>
          <h4 class="text-md leading-3 text-gray-900">
            {{ props.event?.description }}
          </h4>
          <p class="mt-2 max-w-4xl text-lg text-gray-500">
            Für {{ props.event?.normPortions }} Normpersonen
          </p>
        </div>
        <div v-if="!isShoppingRoute" class="mt-3 flex sm:mt-0 sm:ml-4">
          <router-link
            class="text-sm font-medium text-gray-500 hover:text-gray-700"
            :to="{ name: 'EventShoppingCart' }"
          >
            <button
              type="button"
              class="inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Einkaufsliste ansehen
            </button>
          </router-link>
          <button
            v-if="props.event.allowEdit"
            @click="onEditClicked(props.event)"
            type="button"
            class="ml-3 inline-flex items-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Veranstaltung bearbeiten
          </button>
        </div>
      </div>

      <main class="pt-4 pb-16">
        <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div class="px-0">
            <slot />
          </div>
        </div>
      </main>
    </div>
    <div v-else>
      <LoadingItem/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";

import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";

const getDailyFactor = computed(() => {
  if (props?.event?.mealDays?.length > 0) {
    return props.event.mealDays[0].energyKj / 11765;
  }
  return 0;
});

const emit = defineEmits(["onDeleteClicked", "onEditClicked"]);

function onDeleteClicked() {
  emit("onDeleteClicked");
}

function onEditClicked(items: any) {
  emit("onEditClicked", items);
}
const route = useRoute();

const isShoppingRoute = computed(() => {
  return route.name === "EventShoppingCart";
});

const isLoading = computed(() => {
  return !props.event?.event?.name;
});

const pages = computed(() => {
  return [
    { name: "Alle Veranstaltungen", link: "MealDayStart", current: false },
    {
      name: `${props.event?.description} - ${props.event?.event?.name}`,
      link: "EventDefault",
      params: props.event?.id,
      current: false,
    },
  ];
});

const props = defineProps({
  event: { type: Object, required: true },
});
</script>