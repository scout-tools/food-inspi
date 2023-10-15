<template>
  <TabWrapper>
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
        <h1>Du hast noch keine Veranstaltung erstellt.</h1>
        <PrimaryButton v-if="isAuth" class="mx-3 my-3" @click="onLoginclicked"
          >Einloggen</PrimaryButton
        >
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
import { ref, onMounted, computed } from "vue";
import SimpleList from "@/components/list/SimpleList.vue";
import TabWrapper from "@/components/base/TabWrapper.vue";
import MealListItem from "@/modules/meal/components/MealListItem.vue";
import EventAddEdit from "@/modules/meal/components/EventAddEdit/EventAddEdit.vue";
import PrimaryButton from "@/components/button/Primary.vue";

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const events = ref([]);
const isLoading = ref(false);

const eventFiltered = computed(() => {
  return events.value;
});

import { useAuthStore } from "@/modules/auth/store/index.ts";
const authStore = useAuthStore();

function onLoginclicked() {
  authStore.login();
}

async function loadData() {
  isLoading.value = true;
  const response = await mealStore.fetchMyEventsSmall();
  events.value = response.data;
  isLoading.value = false;
}

const openEventAddEdit = ref(false);

function onEventAddClicked() {
  openEventAddEdit.value = true;
}

function onEventAddEditClose() {
  openEventAddEdit.value = false;
}

const isAuth = computed(() => {
  return authStore.isAuth;
});
onMounted(async () => {
  await loadData();
});
</script>
