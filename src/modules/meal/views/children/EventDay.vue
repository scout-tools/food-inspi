<template>
  <div class="mx-auto mt-6 max-w-5xl px-4 sm:px-6 lg:px-8">
    <div class="bg-white px-4 py-5 sm:px-6">
      <div class="min-w-0 flex-1">
        <h2 class="text-lg font-medium leading-6 text-gray-900 mx-4 my-2">
          Tag: {{ moment(getMealDay(event).date).format("dddd") }} -
          {{ moment(getMealDay(event).date).format("LL") }}
        </h2>
        <h3 class="text-lg font-medium leading-6 text-gray-900 mx-4 my-2">
          Tagesengerie: {{ getMealDay(event).energyKj }} kJ von 13.125 kJ
        </h3>
        <!-- <a
              href="#"
              class="
                relative
                inline-flex
                items-center
                rounded-l-md
                border border-gray-300
                bg-white
                px-4
                py-2
                text-sm
                font-medium
                text-gray-500
                hover:bg-gray-50
                focus:z-10
                focus:border-blue-600
                focus:outline-none
                focus:ring-1
                focus:ring-blue-600
              "
            >
              <span class="sr-only">Next</span>
              <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
            </a>
            <a
              href="#"
              class="
                relative
                -ml-px
                inline-flex
                items-center
                rounded-r-md
                border border-gray-300
                bg-white
                px-4
                py-2
                text-sm
                font-medium
                text-gray-500
                hover:bg-gray-50
                focus:z-10
                focus:border-blue-600
                focus:outline-none
                focus:ring-1
                focus:ring-blue-600
              "
            >
              <span class="sr-only">Previous</span>
              <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
            </a> -->
      </div>
    </div>
    <ul role="list" class="grid grid-cols-1 gap-6">
      <MealList
        class="my-2 mx-2"
        v-for="meal in getMeal(event)"
        :meal="meal"
        :key="meal.id"
        @onItemUpdate="onMealUpdate"
        @onAddMealItemClicked="onAddMealItemClicked"
        @onMenuItemUpdate="onMealItemUpdate"
      />
      <MealListEmpty @onAddClicked="onAddMealClicked" />
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
import localization from "moment/locale/de";

moment.updateLocale("de", localization);

import { ref, watch, onMounted, computed } from "vue";
import EmptyItem from "@/modules/recipe/components/simulator/EmptyItem.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import MealList from "@/modules/meal/components/MealList.vue";
import MealListEmpty from "@/modules/meal/components/MealListEmpty.vue";
import Container from "@/modules/meal/components/Container.vue";

import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

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
  return mealStore.event;
});

const buttonList = [{ name: "Neue Zutat", linkName: "IngredientCreate" }];

const mealStore = useMealStore();

function getMeal(event) {
  if (event && event.mealDays && event.mealDays.length > 0) {
    console.log(event);
    console.log(event?.mealDays[0].meals);
    return event?.mealDays[0].meals;
  }
  return [];
}

function getMealDay(event) {
  if (event && event.mealDays && event.mealDays.length > 0) {
    return event?.mealDays[0];
  }
  return [];
}

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchEventById(id);
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
