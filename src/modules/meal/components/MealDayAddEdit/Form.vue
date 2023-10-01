<template>
  <div>
    <div v-if="!loading">
      <BaseField
        component="Select"
        label="Tag Aktivitätsfaktor"
        techName="activityFactor"
        v-model="state.activityFactor"
        :items="physicalActivities"
        :errors="errors.activityFactor?.$errors"
      />
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

import { reactive, onMounted, ref, watch, computed } from "vue";
import BaseField from "@/components/field/Base.vue";
import Select from "@/components/field/Select.vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";

import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  id: 1,
  mealEvent: null,
  activityFactor: null,
  maxDayPartFactor: null,
  date: null,
});

const rules = {
  activityFactor: {
    required,
  },
  maxDayPartFactor: {
    required,
  },
};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(false);

const loading = computed(() => {
  return isLoading.value;
});

const mealStore = useMealStore();

const physicalActivities = computed(() => {
  return mealStore.physicalActivity;
});

const isEdit = computed(() => {
  return !!props.items?.id;
});

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
      activityFactor: state.activityFactor.id,
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

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

async function updateData() {
  isLoading.value = true;

  await Promise.all([mealStore.fetchPhysicalActivity()]);
  state.maxDayPartFactor = props.items?.maxDayPartFactor;
  state.activityFactor = physicalActivities.value.filter(
      (item) => item.id === props.items?.activityFactor
    )[0];
  isLoading.value = false;
}

onMounted(() => {
  updateData();
});
</script>
