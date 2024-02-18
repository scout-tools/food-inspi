<template>
  <div v-if="!isLoading">
    <div v-for="item in props.items?.meal?.mealItems" :key="item.id">
      {{ item.factor }} x {{ item.recipe.name }} ({{ item.energyKj }} kJ,
      {{ (item.priceEur || 0).toFixed(2) }} €)
      <div class="relative mb-12">
        <label for="labels-range-input" class="sr-only">Labels range</label>
        <input
          id="labels-range-input"
          type="range"
          v-model="item.factor"
          min="0.0"
          max="2.0"
          step="0.01"
          class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
        <span class="text-sm text-gray-500 absolute start-0 -bottom-6">
          Nichts (0.0)</span
        >
        <span
          class="text-sm text-gray-500 absolute start-1/2 -translate-x-1/2 -bottom-6"
          >Jeder eine (1.0)</span
        >
        <span class="text-sm text-gray-500 absolute end-0 -bottom-6"
          >Jeder zwei (2.0)</span
        >
      </div>
    </div>
    <PrimaryButton @click="onSaveClicked" :label="'Elemente neu justieren'" />
  </div>
  <LoadingItem v-else />
</template>
  
<script setup lang="ts">
import { reactive, onMounted, ref, computed } from "vue";

import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

import BaseField from "@/components/field/Base.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

const state = reactive({
  name: "Test",
});

const rules = {};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const errors = ref([]);
const isLoading = ref(true);
const emit = defineEmits(["close"]);

const mealStore = useMealStore();

async function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  let id = Number(route.params.id);
  let eventDayId = Number(route.params.eventDayId);

  for (let item of props.items.meal.mealItems) {
    await mealStore.updatePartical({
      id: item.id,
      factor: item.factor,
    });
  }
  onCloseClicked();
}

function goToRecipe(route: string, params: any) {
  router.push({
    name: route,
    params: params,
  });
  if (router.currentRoute.value.name === route) {
    router.go(router.currentRoute.value);
  }
}


    
  const onCloseClicked = () => {
    emit("close");
  };

onMounted(async () => {
  await mealStore.fetchMealTypes();
  isLoading.value = false;
});
</script>
  