<template>
  <div>
    <div v-if="!loading">
      <BaseField
        component="Number"
        label="Tagesaktor"
        techName="maxDayPartFactor"
        v-model="state.maxDayPartFactor"
        :errors="errors.maxDayPartFactor?.$errors"
      />
      <PrimaryButton @click="onSaveClicked" :label="'Tag bearbeiten'" />
    </div>
    <LoadingItem v-else />
  </div>
</template>

<script setup lang="ts">
import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

import { reactive, onMounted, ref, computed } from "vue";
import BaseField from "@/components/field/Base.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";

import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required } from "@vuelidate/validators";

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

const state = reactive({
  id: 1,
  mealEvent: null,
  maxDayPartFactor: null,
  date: null,
});

const rules = {
  maxDayPartFactor: {
    required,
  },
};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const errors = ref([]);
const isLoading = ref(false);

const loading = computed(() => {
  return isLoading.value;
});

const mealStore = useMealStore();

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  let id = Number(route.params.id);
  let eventDayId = Number(route.params.eventDayId);
  isLoading.value = true;
  mealStore
    .updateMealDay({
      id: props.items?.id,
      mealEvent: props.items?.mealEvent,
      maxDayPartFactor: state.maxDayPartFactor,
      date: props.items?.date,
    })
    .then((response2: any) => {
      goToRecipe("EventDay", {
        id,
        eventDayId,
      });
    });
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

async function updateData() {
  isLoading.value = true;

  await Promise.all([mealStore.fetchPhysicalActivity()]);
  state.maxDayPartFactor = props.items?.maxDayPartFactor;
  isLoading.value = false;
}

onMounted(() => {
  updateData();
});
</script>
