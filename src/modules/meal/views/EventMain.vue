<template>
  <div class="2xl:px-64 xl:px-30">
    <Container
      :event="eventData"
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
const isLoading = ref(false);
const eventData = ref({});

function onEventUpdateClicked(items: Object) {
  openEventAddEdit.value = true;
  eventData.value = items;
}

function onEventClosedClicked() {
  openEventAddEdit.value = false;
  eventData.value = {};
}

const mealStore = useMealStore();

onMounted(async() => {
  isLoading.value = true;
  const id = route.params.id;
  const response = await mealStore.fetchEventById(id);
  eventData.value = response.data;
  isLoading.value = false;
});

</script>
