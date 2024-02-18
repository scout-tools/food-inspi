<template>
  <div>
<div v-if="!isLoading">
  <div class="mx-auto mt-6 max-w-5xl px-4 sm:px-6 lg:px-8">
    <div class="bg-gray-50 pt-4 sm:pt-4">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-4xl text-center">
          <h2 class="text-2xl font-bold tracking-tight text-gray-900">
            Tagesübersicht
          </h2>
          <button v-if="event?.allowEdit" @click="onMealDayUpdate(mealDay)" class="text-sm text-blue-600 hover:text-blue-500">
            Tag bearbeiten
          </button>
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
                          (mealDay.energyKjSum)) *
                        100
                      ).toFixed(0)
                    }}
                    %
                  </dd>
                  <dd class="order-2 text-sm tracking-tight text-blue-500">
                    {{ (mealDay.energyKj).toFixed(0) }} kJ /
                    {{ (mealDay.energyKjSum).toFixed(0) }} kJ
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
        @onAdjustBuffetClicked="onAdjustBuffetClicked"
        @onMealCloneClicked="onMealCloneClicked"
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
    <MealClone
      :open="openMealCloneForm"
      @close="onMealCloneClosed"
      :items="mealCloneFormData"
      header="Menü klonen"
    />
    <MealDayAddEdit
      :open="openMealDayForm"
      @close="onMealDayClose"
      :items="mealDayData"
      header="Tag editieren"
    />
    <AdjustBuffetEdit
      :open="openAdjustBuffet"
      @close="openAdjustBuffetClosed"
      :items="adjustBuffetData"
      header="Buffet anpassen"
    />
  </div>
</div>
  <div v-else>
    <LoadingItem/>
  </div>
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

import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

function openAdjustBuffetClosed() {
  const eventId = route.params.id;
  openAdjustBuffet.value = false;
  adjustBuffetData.value = {};
  mealStore.fetchEventById(eventId);
  commonStore.showSuccess("Buffet erfolgreich angepasst");
}

// MenuItem Sidebar

import MealItemAddEdit from "@/modules/meal/components/MealItemAddEdit/MealItemAddEdit.vue";
import MealClone from "@/modules/meal/components/mealClone/MealClone.vue";
import MealDayAddEdit from "@/modules/meal/components/MealDayAddEdit/MealDayAddEdit.vue";
import AdjustBuffetEdit from "@/modules/meal/components/adjustBuffetEdit/AdjustBuffetEdit.vue";

const openMealItemForm = ref(false);
const openMealDayForm = ref(false);
const openMealCloneForm = ref(false);
const openAdjustBuffet = ref(false)
const mealItemData = ref({});
const mealDayData = ref({});
const mealCloneFormData = ref({});
const adjustBuffetData = ref({});


function onMealDayUpdate(items: Object) {
  openMealDayForm.value = true;
  mealDayData.value = items;
}

function onMealDayClose() {
  openMealDayForm.value = false;
  mealDayData.value = {};
}

function onAddMealItemClicked(items: Object) {
  openMealItemForm.value = true;
  mealItemData.value = items;
}

function onAdjustBuffetClicked(items: Object) {
  openAdjustBuffet.value = true;
  adjustBuffetData.value = items;
}

function onMealCloneClicked(items: Object) {
  openMealCloneForm.value = true;
  mealCloneFormData.value = items;
}

function onMealCloneClosed() {
  mealCloneFormData.value = {};
  openMealCloneForm.value = false;
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
  const eventDayId = route.params.eventDayId;
  return mealStore?.mealEvent?.mealDays?.find((mealDay) => mealDay.id == eventDayId);
});

const buttonList = [{ name: "Neue Zutat", linkName: "IngredientCreate" }];


function getMeal(event) {
  if (event && event.mealDays && event.mealDays.length > 0) {
    return event?.mealDays[0].meals;
  }
  return [];
}

const isLoading = computed(() => {
  return !mealDay.value.date
});

function onUpdateMealDayClicked() {
}


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
  ReceiptPercentIcon,
} from "@heroicons/vue/24/outline";
import {
  EnvelopeIcon,
  FunnelIcon,
  MagnifyingGlassIcon,
  PhoneIcon,
} from "@heroicons/vue/20/solid";
import { al } from "vitest/dist/reporters-5f784f42";
import common from "mocha/lib/interfaces/common";

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
