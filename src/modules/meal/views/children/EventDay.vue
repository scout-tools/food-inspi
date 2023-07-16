<template>
  <div class="mx-auto mt-6 max-w-5xl px-4 sm:px-6 lg:px-8">
    <div class="bg-gray-50 pt-4 sm:pt-4">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-4xl text-center">
          <h2 class="text-2xl font-bold tracking-tight text-gray-900">
            Tagesübersicht
          </h2>
          <p class="mt-3 text-lg text-gray-500 sm:mt-4">
            {{ $dayjs(mealDay.date).format("dddd") }} -
            {{ $dayjs(mealDay.date).format("LL") }}
          </p>
        </div>
      </div>
      <div class="mt-10 bg-white pb-12 sm:pb-16">
        <div class="relative">
          <div class="absolute inset-0 h-1/2 bg-gray-50" />
          <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="mx-auto max-w-4xl">
              <dl class="rounded-lg bg-white shadow-lg sm:grid sm:grid-cols-4">
                <div
                  class="
                    flex flex-col
                    border-b border-gray-100
                    p-6
                    text-center
                    sm:border-0 sm:border-r
                  "
                >
                  <dt
                    class="
                      order-1
                      mt-2
                      text-sm
                      font-medium
                      leading-6
                      text-gray-500
                    "
                  >
                    Soll Tagesenergie
                  </dt>
                  <dd
                    class="
                      order-0
                      text-2xl
                      font-bold
                      tracking-tight
                      text-blue-600
                    "
                  >
                    {{
                      (
                        (mealDay.energyKj /
                          (11765 * mealDay.maxDayPartFactor)) *
                        100
                      ).toFixed(0)
                    }}
                    %
                  </dd>
                  <dd class="order-2 text-sm tracking-tight text-blue-500">
                    {{ mealDay.energyKj }} kJ /
                    {{ 11765 * mealDay.maxDayPartFactor }} kJ
                  </dd>
                </div>
                <div
                  class="
                    flex flex-col
                    border-b border-gray-100
                    p-6
                    text-center
                    sm:border-0 sm:border-r
                  "
                >
                  <dt
                    class="
                      order-1
                      mt-2
                      text-sm
                      font-medium
                      leading-6
                      text-gray-500
                    "
                  >
                    Soll Tagesfaktor
                  </dt>
                  <dd
                    class="
                      order-0
                      text-2xl
                      font-bold
                      tracking-tight
                      text-blue-600
                    "
                  >
                    {{ (mealDay.dayFactors * 100).toFixed(0) }} /
                    {{ (mealDay.maxDayPartFactor * 100).toFixed(0) }} %
                  </dd>
                </div>
                <div
                  class="
                    flex flex-col
                    border-t border-b border-gray-100
                    p-6
                    text-center
                    sm:border-0 sm:border-l sm:border-r
                  "
                >
                  <dt
                    class="
                      order-2
                      mt-2
                      text-sm
                      font-medium
                      leading-6
                      text-gray-500
                    "
                  >
                    Tagespreis
                  </dt>
                  <dd
                    class="
                      order-1
                      text-2xl
                      font-bold
                      tracking-tight
                      text-blue-600
                    "
                  >
                    {{ (mealDay?.priceEur || 0).toFixed(2) }} €
                  </dd>
                </div>
                <div
                  class="
                    flex flex-col
                    border-t border-gray-100
                    p-6
                    text-center
                    sm:border-0 sm:border-l
                  "
                >
                  <dt
                    class="
                      order-2
                      mt-2
                      text-sm
                      font-medium
                      leading-6
                      text-gray-500
                    "
                  >
                    Tages Nutri-Score
                  </dt>
                  <dd
                    class="
                      order-1
                      text-2xl
                      font-bold
                      tracking-tight
                      text-blue-600
                    "
                  >
                    <NutriSlim :nutriClass="mealDay.nutriClass" />
                  </dd>
                </div>
              </dl>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ul role="list" class="grid grid-cols-1 gap-6">
      <MealList
        class="my-2 mx-2"
        v-for="meal in mealDay.meals"
        :meal="meal"
        :key="meal.id"
        @onItemUpdate="onMealUpdate"
        @onAddMealItemClicked="onAddMealItemClicked"
        @onMenuItemUpdate="onMealItemUpdate"
      />
      <MealListEmpty v-if="event?.allowEdit" @onAddClicked="onAddMealClicked" />
    </ul>
    <MealAddEdit
      :open="openMealForm"
      @close="onMealFormClose"
      :items="mealData"
      header="Menü"
    />
    <MealItemAddEdit
      :open="openMealItemForm"
      @close="onMealItemClose"
      :items="mealItemData"
      header="Neue Rezept zum Menü hinzufügen"
    />
  </div>
</template>

<script setup lang="ts">
import moment from "moment";

import { ref, watch, onMounted, computed } from "vue";
import EmptyItem from "@/modules/recipe/components/simulator/EmptyItem.vue";
import MealList from "@/modules/meal/components/MealList.vue";
import MealListEmpty from "@/modules/meal/components/MealListEmpty.vue";
import Container from "@/modules/meal/components/Container.vue";
import NutriSlim from "@/components/score/NutriSlim.vue";

import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const route = useRoute();

// Menu-Sidebar
import MealAddEdit from "@/modules/meal/components/MealAddEdit/MealAddEdit.vue";

const openMealForm = ref(false);
const mealData = ref({});

function onAddMealClicked() {
  openMealForm.value = true;
  mealData.value = {};
}

function onMealUpdate(items: Object) {
  openMealForm.value = true;
  mealData.value = items;
}

function onMealFormClose() {
  openMealForm.value = false;
  mealData.value = {};
}

// MenuItem Sidebar

import MealItemAddEdit from "@/modules/meal/components/MealItemAddEdit/MealItemAddEdit.vue";

const openMealItemForm = ref(false);
const mealItemData = ref({});

function onAddMealItemClicked(items: Object) {
  openMealItemForm.value = true;
  mealItemData.value = items;
}

function onMealItemUpdate(items: Object) {
  openMealItemForm.value = true;
  mealItemData.value = items;
}

function onMealItemClose() {
  openMealItemForm.value = false;
  mealItemData.value = {};
}

// -

const event = computed(() => {
  return mealStore.mealEvent;
});

const mealDay = computed(() => {
  return mealStore.mealDay;
});

const buttonList = [{ name: "Neue Zutat", linkName: "IngredientCreate" }];


function getMeal(event) {
  if (event && event.mealDays && event.mealDays.length > 0) {
    return event?.mealDays[0].meals;
  }
  return [];
}

onMounted(() => {
  const id = route.params.eventDayId;
  mealStore.fetchMealDayById(id);
});

import {
  Dialog,
  DialogPanel,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import {
  Bars3Icon,
  CalendarIcon,
  CogIcon,
  HomeIcon,
  MagnifyingGlassCircleIcon,
  MapIcon,
  MegaphoneIcon,
  SquaresPlusIcon,
  UserGroupIcon,
  XMarkIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "@heroicons/vue/24/outline";
import {
  EnvelopeIcon,
  FunnelIcon,
  MagnifyingGlassIcon,
  PhoneIcon,
} from "@heroicons/vue/20/solid";

const eventFields = [
  {
    key: "name",
    display: "Veranstaltungsname",
  },
  {
    key: "normPortions",
    display: "Norm Portionen",
  },
];

const mealDayFields = [
  {
    key: "activityFacor",
    display: "Aktivitätsfaktor",
  },
  {
    key: "date",
    display: "Datum",
  },
];
const sidebarOpen = ref(false);
</script>
