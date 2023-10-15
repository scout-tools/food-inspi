<template>
  <div class="flex h-full flex-col">
    <div
      v-if="mealItems2 && mealItems2.length > 3 && eventDays && dayHours"
      ref="container"
      class="isolate flex flex-auto flex-col overflow-auto bg-white"
    >
      <div
        style="width: 165%"
        class="flex max-w-full flex-none flex-col sm:max-w-none md:max-w-full"
      >
        <div
          ref="containerNav"
          class="sticky top-0 z-30 flex-none bg-white shadow ring-1 ring-black ring-opacity-5 sm:pr-8"
        >
          <div
            class="-mr-px hidden divide-x divide-gray-100 border-r border-gray-100 text-sm leading-6 text-gray-500 sm:grid"
            :class="`grid-cols-${eventDays.length}`"
          >
            <div class="col-end-1 w-14" />
            <div
              v-for="day in eventDays"
              class="flex items-center justify-center py-3"
            >
              <span
                >Mon
                <span
                  class="items-center justify-center font-semibold text-gray-900"
                  >{{ day }}</span
                ></span
              >
            </div>
          </div>
        </div>
        <div class="flex flex-auto">
          <div
            class="sticky left-0 z-10 w-14 flex-none bg-white ring-1 ring-gray-100"
          />
          <div class="grid flex-auto grid-cols-1 grid-rows-1">
            <!-- Horizontal lines -->
            <div
              class="col-start-1 col-end-2 row-start-1 grid divide-y divide-gray-100"
              style="grid-template-rows: repeat(15, minmax(3.5rem, 1fr))"
            >
              <div ref="containerOffset" class="row-end-1 h-7" />
              <div v-for="hour in dayHours" :key="hour.id">
                <div
                  class="sticky left-0 z-20 -ml-14 -mt-2.5 w-14 pr-2 text-right text-xs leading-5 text-gray-400"
                >
                  {{ hour }} Uhr
                </div>
              </div>
              <div />
            </div>

            <!-- Vertical lines -->
            <div
              class="col-start-1 col-end-2 row-start-1 hidden grid-rows-1 divide-x divide-gray-100 sm:grid"
              :class="`grid-cols-${eventDays.length}`"
            >
              <div class="col-start-1 row-span-full" />
              <div class="col-start-2 row-span-full" />
              <div class="col-start-3 row-span-full" />
            </div>

            <!-- Events -->
            <ol
              class="col-start-1 col-end-2 row-start-1 grid"
              :class="`grid-cols-3`"
              style="
                grid-template-rows: 1.5rem repeat(288, minmax(0, 1fr)) auto;
              "
            >
              <li
                class="relative mt-px flex"
                :class="`sm:col-start-${meal.day}`"
                :style="`grid-row: ${3 + ((meal.start) * 14)} / span ${(meal.end - meal.start) * 19}`"
                v-for="meal in mealItems2"
                :key="meal.id"
              >
                <a
                  href="#"
                  class="group absolute inset-1 flex flex-col overflow-y-auto rounded-lg bg-blue-50 p-2 text-xs leading-5 hover:bg-blue-100"
                >
                  <p class="order-1 font-semibold text-blue-700">
                    {{ meal.name }}
                  </p>
                  <p class="text-blue-500 group-hover:text-blue-700">
                    <time datetime="2022-01-12T06:00">{{ meal.start + 7}} Uhr</time>
                  </p>
                </a>
              </li>
            </ol>
          </div>
        </div>
      </div>
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
import { c } from "vitest/dist/reporters-5f784f42";

const mealStore = useMealStore();

// const container = ref(null);
// const containerNav = ref(null);
// const containerOffset = ref(null);

const route = useRoute();

const event = computed(() => {
  return mealStore.mealEvent;
});

const eventDays = computed(() => {
  let days = [];
  mealStore?.mealEvent?.mealDays.forEach((day) => {
    days.push(day.date);
  });
  console.log(days);
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
  let mealItems = [
    {
      id: 1,
      name: "Breakfast1",
      start: 1,
      end: 2,
      day: 1,
    },
    {
      id: 3,
      name: "Dinner1",
      start: 10,
      end: 11,
      day: 1,
    },
    {
      id: 4,
      name: "Breakfast2",
      start: 1,
      end: 3,
      day: 2,
    },
    {
      id: 6,
      name: "Dinner2",
      start: 10,
      end: 11,
      day: 2,
    },
    {
      id: 9,
      name: "Dinner3",
      start: 10,
      end: 11,
      day: 3,
    },
  ];
  console.log(mealItems);
  return mealItems;
});

const mealItems2 = computed(() => {
  let mealItems = [];
  let id = 1;
  mealStore?.mealEvent?.mealDays.forEach((day, dayIndex) => {
    day.meals.forEach((meal) => {
      const startDate = parseInt(meal.timeStart.split(":")[0], 10);
      const endDate = parseInt(meal.timeEnd.split(":")[0], 10);
      if (endDate - startDate < 3) {
        mealItems.push({
        id,
        name: meal.name,
        start: startDate - 7,
        end: endDate - 7,
        day: eventDays.value.indexOf(meal.mealDay.date) + 1,
      });
      id = id + 1;
      }
    });
  });
  console.log(mealItems);
  return mealItems;
});
</script>
  