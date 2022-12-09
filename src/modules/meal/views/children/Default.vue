<template>
  <div>
    <div v-for="day in event.mealDays" :key="day.id">
      <div class="overflow-hidden bg-white shadow sm:rounded-md">
        <ul role="list" class="divide-y divide-gray-200">
          <li v-for="day in event.mealDays" :key="day.id">
            <router-link
              :to="{
                name: 'EventDay',
                params: { id: event.id, eventDayId: day.id },
              }"
              class="block hover:bg-gray-50"
            >
              <div class="flex items-center px-4 py-4 sm:px-6">
                <div class="flex min-w-0 flex-1 items-center">
                  <div
                    class="min-w-0 flex-1 px-4 md:grid md:grid-cols-2 md:gap-4"
                  >
                    <div>
                      <p class="truncate text-sm font-medium text-indigo-600">
                        {{ moment(day.date).format("dddd") }}
                      </p>
                      <p class="mt-2 flex items-center text-sm text-gray-500">
                        <BoltIcon
                          class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
                          aria-hidden="true"
                        />
                        <span class="truncate"
                          >{{ day.energyKj }} kJ / 14000 kJ</span
                        >
                      </p>
                    </div>
                    <div class="hidden md:block">
                      <div>
                        <p class="text-sm text-gray-900">
                          {{ " " }}
                          <time :datetime="day.date">{{
                            moment(day.date).format("LL")
                          }}</time>
                        </p>
                        <p class="mt-2 flex items-center text-sm text-gray-500">
                          <CheckCircleIcon
                            class="mr-1.5 h-5 w-5 flex-shrink-0 text-green-400"
                            aria-hidden="true"
                          />
                          {{ day.meals.length }} Mahlzeiten
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
                <div>
                  <ChevronRightIcon
                    class="h-5 w-5 text-gray-400"
                    aria-hidden="true"
                  />
                </div>
              </div>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
    <div v-if="event.mealDays && !event.mealDays.length">
      Noch kein Tag vorhanden.
    </div>
  </div>
</template>


<script setup lang="ts">
import moment from "moment";

import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

import {} from "@headlessui/vue";

import {
  BoltIcon,
  CheckCircleIcon,
  ChevronRightIcon,
} from "@heroicons/vue/20/solid";

const sidebarOpen = ref(false);

const route = useRoute();

const mealStore = useMealStore();

const buttonList = [{ name: "Neue Zutat", linkName: "IngredientCreate" }];

const event = computed(() => {
  return mealStore.event;
});

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchEventById(id);
});
</script>


