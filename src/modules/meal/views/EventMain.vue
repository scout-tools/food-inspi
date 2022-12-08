<template>
  <div>
    <Container
      :event="event"
      :eventFields="eventFields"
      @onDeleteClicked="onEventClosedClicked"
      @onEditClicked="onEventUpdateClicked"
    >
      <router-view />
    </Container>
    <EventAddEdit
      :open="openEventAddEdit"
      :items="eventData"
      @close="onEventClosedClicked"
      header="Veranstaltung"
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
import EventAddEdit from "@/modules/meal/components/EventAddEdit/EventAddEdit.vue";

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

// Event Sidebar


const openEventAddEdit = ref(false);
const eventData = ref({});

function onEventAddClicked() {
  openEventAddEdit.value = true;
  eventData.value = {};
}

function onEventUpdateClicked(items: Object) {
  openEventAddEdit.value = true;
  eventData.value = items;
}

function onEventClosedClicked() {
  openEventAddEdit.value = false;
  eventData.value = {};
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
