<template>
  <div>
    <div v-if="!isLoading">
      <BaseField
        component="AutoComplete"
        label="Veranstaltungen"
        techName="event"
        v-model="state.event"
        :items="events"
        :errors="errors.event?.$errors"
        :lookupListDisplay="['description']"
        :searchField="['description']"
      />
      <BaseField
        v-if="state.event"
        component="AutoComplete"
        label="Tag"
        techName="eventDay"
        v-model="state.eventDay"
        :items="eventDays"
        :errors="errors.eventDay?.$errors"
        :lookupListDisplay="['date']"
        :searchField="['date']"
      />
      <BaseField
        v-if="state.eventDay"
        component="AutoComplete"
        label="Menü"
        techName="meal"
        v-model="state.meal"
        :items="meals"
        :errors="errors.meal?.$errors"
        :lookupListDisplay="['name', 'getMealTypeDisplay']"
        :searchField="['name', 'getMealTypeDisplay']"
      />
      <PrimaryButton @click="onSaveClicked" :label="'Menü übernehmen'" />
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
  event: null,
  eventDay: null,
  meal: null,
});

const rules = {
  event: {
    required,
  },
  eventDay: {
    required,
  },
  meal: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

const errors = ref([]);
const events = ref([]);
const isLoading = ref(false);

const eventDays = computed(() => {
  return state.event.mealDays;
});

const meals = computed(() => {
  return state.eventDay?.meals;
});

const recipeStore = useRecipeStore();

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
    .cloneMeal({
      mealId: props.items.meal.id,
      clone_meal_id: state?.meal?.id,
    })
    .then((response2: any) => {
      goToRecipe("EventDay", {
        id,
        eventDayId,
      });
    });
  isLoading.value = false;
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

const props = defineProps({
  items: { type: Object, required: true },
});

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

onMounted(async () => {
  isLoading.value = true;
  const response = await mealStore.fetchPublicEvents();

  events.value = response.data;

  isLoading.value = false;
});
</script>
