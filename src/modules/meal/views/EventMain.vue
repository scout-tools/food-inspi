<template>
  <div class="2xl:px-64 xl:px-30">
    <Container
      :event="event"
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

import { ref, watch, onMounted, computed } from "vue";
import Container from "@/modules/meal/components/Container.vue";
import EventAddEdit from "@/modules/meal/components/EventAddEdit/EventAddEdit.vue";


import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

const route = useRoute();

const openEventAddEdit = ref(false);
const eventData = ref({});

function onEventUpdateClicked(items: Object) {
  openEventAddEdit.value = true;
  eventData.value = items;
}

function onEventClosedClicked() {
  openEventAddEdit.value = false;
  eventData.value = {};
}

const event = computed(() => {
  return mealStore.event;
});


const mealStore = useMealStore();

const sidebarOpen = ref(false);

onMounted(() => {
  const id = route.params.id;
  mealStore.fetchEventById(id);
});

</script>
