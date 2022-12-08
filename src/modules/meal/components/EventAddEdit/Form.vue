<template>
  <div>
    <BaseField
      component="Text"
      label="Name"
      techName="name"
      v-model="state.name"
      :errors="errors.name?.$errors"
    />
    <BaseField
      component="Number"
      v-model="state.normPortions"
      techName="normPortions"
      label="Anzahl Portionen"
      :errors="errors.normPortions?.$errors"
    />
    <BaseField
      v-if="!isEdit"
      component="Date"
      label="Datum"
      techName="date"
      v-model="state.date"
      :errors="errors.date?.$errors"
    />
    <PrimaryButton
      @click="onSaveClicked"
      :label="!isEdit ? 'Veranst. hinzufügen' : 'Veranst. bearbeiten'"
    />
    <PrimaryButton
      v-if="isEdit"
      class="mx-2 my-2"
      @click="onDeleteClicked()"
      color="red"
      label="Veranst löschen"
    />
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
import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  id: null,
  name: '',
  normPortions: 1,
  date: null,
});

const rules = {
  name: {
    required,
  },
  normPortions: {
    required,
  }
};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(false);

const mealStore = useMealStore();

const isEdit = computed(() => {
  return !!props.items?.id;
});


function onDeleteClicked() {
  mealStore.deleteEvent(props.items).then((response) => {
    router.push({
      name: "MealDayStart",
    });
  });
}

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  // new
  if (!isEdit.value) {
    mealStore.createEvent({
      name: state.name,
      normPortions: state.normPortions,
      date: state.date
    }).then((response: any) => {
      router.push({
        name: "EventDay",
        params: {
          id: response.data.id,
          eventDayId: response.data.mealDays[0].id,
        },
      });
    });
  } else {
    mealStore.updateEvent({
      id: state.id,
      name: state.name,
      normPortions: state.normPortions,
    }).then((response: any) => {
      goToRecipe(response.data.id)
    });
  }
}

function goToRecipe(id: number) {
  router.push({
    name: "EventDefault",
    params: {
      id: id,
    },
  });
  if (router.currentRoute.value.name === "EventDefault") {
    router.go(router.currentRoute.value);
  }
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

onMounted(() => {
  if (isEdit.value) {
    state.id = props.items?.id;
    state.name = props.items?.name;
    state.normPortions = props.items?.normPortions;
  } else {
    state.name = null;
    state.normPortions = 1;
  }
});
</script>
