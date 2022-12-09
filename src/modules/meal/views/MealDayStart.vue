<template>
  <div class="2xl:px-64 xl:px-30">
    <EmptyItem @onAddClicked="onEventAddClicked" />
    <EventAddEdit
      :open="openEventAddEdit"
      @close="onEventAddEditClose"
      header="Veranstaltung"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import EmptyItem from "@/modules/meal/components/editor/EmptyItem.vue";
import EventAddEdit from "@/modules/meal/components/EventAddEdit/EventAddEdit.vue";
import { useRoute } from "vue-router";
import { useMealStore } from "@/modules/meal/store/index";

const route = useRoute();

const openEventAddEdit = ref(false);

const mealStore = useMealStore();
const events = computed(() => {
  return mealStore.events;
});

function onEventAddClicked() {
  openEventAddEdit.value = true;
}

function onEventAddEditClose() {
  openEventAddEdit.value = false;
}
</script>
