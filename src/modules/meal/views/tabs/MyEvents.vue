<template>
  <TabWrapper>
    <div v-if="isAuth">
      <PrimaryButton @click="onEventAddClicked">Neues Event</PrimaryButton>
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
    </div>
    <div v-else>
      <h1>Du bist nicht eingeloggt.</h1>
      <PrimaryButton class="mx-3 my-3" @click="onLoginclicked"
        >Einloggen</PrimaryButton
      >
    </div>
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
  return mealStore.mealEvents
});

const eventFiltered = computed(() => {
  return events.value;
});

function onLoginclicked() {
	authStore.login()
}

const selectedValue = ref("Aktive Anmeldephase");
const openEventAddEdit = ref(false);


const tabs = computed(() => {
  const query = { ...router.currentRoute.value.query };

  return [];
});

function refresh() {
  mealStore.fetchMyEvents();
}

function onEventAddClicked() {
  openEventAddEdit.value = true;
}

function onEventAddEditClose() {
  openEventAddEdit.value = false;
}

import { useAuthStore } from "@/modules/auth/store/index.ts";
const authStore = useAuthStore();

const isAuth = computed(() => {
  return authStore.isAuth;
});


onMounted(() => {
  refresh();
});
</script>

