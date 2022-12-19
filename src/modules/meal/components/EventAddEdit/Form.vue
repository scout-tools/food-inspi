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
      component="TextArea"
      label="Beschreibung"
      techName="description"
      v-model="state.description"
      :errors="errors.description?.$errors"
    />
    <BaseField
      component="Number"
      v-model="state.normPortions"
      techName="normPortions"
      label="Anzahl Portionen"
      :errors="errors.normPortions?.$errors"
    />
    <BaseField
      component="Select"
      v-model="state.activityFactor"
      techName="activityFactor"
      label="Aktivität"
      :items="physicalActivities"
      :errors="errors.activityFactor?.$errors"
    />
    <BaseField
      v-if="!isEdit"
      component="DateTime"
      label="Start-Datum"
      techName="startDate"
      v-model="state.startDate"
      :errors="errors.startDate?.$errors"
    />
    <BaseField
      v-if="!isEdit"
      component="DateTime"
      label="End-Datum"
      techName="endDate"
      v-model="state.endDate"
      :errors="errors.endDate?.$errors"
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
import PrimaryButton from "@/components/button/Primary.vue";
import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  id: null,
  name: "",
  description: "",
  normPortions: 1,
  startDate: null,
  endDate: null,
  activityFactor: null,
});

const rules = {
  name: {
    required,
  },
  normPortions: {
    required,
  },
  startDate: {
    required,
  },
  endDate: {
    required,
  },
  activityFactor: {
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

const mealStore = useMealStore();

const isEdit = computed(() => {
  return !!props.items?.id;
});

const physicalActivities = computed(() => {
  return mealStore.physicalActivity;
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
    mealStore
      .createEvent({
        name: state.name,
        description: state.description,
        normPortions: state.normPortions,
        startDate: state.startDate,
        endDate: state.endDate,
        activityFactor: state.activityFactor.id,
      })
      .then((response: any) => {
        debugger;
        goToRecipe(response.data.id)
      });
  } else {
    mealStore
      .updateEvent({
        id: state.id,
        name: state.name,
        description: state.description,
        normPortions: state.normPortions,
        startDate: state.startDate,
        endDate: state.endDate,
        activityFactor: state.activityFactor.id,
      })
      .then((response: any) => {
        goToRecipe(response.data.id);
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
  mealStore.fetchPhysicalActivity();
  setTimeout(function () {
    if (isEdit.value) {
      state.id = props.items?.id;
      state.name = props.items?.name;
      state.description = props.items?.description;
      state.normPortions = props.items?.normPortions;
      state.startDate = props.items?.startDate;
      state.endDate = props.items?.endDate;
      state.activityFactor = physicalActivities.value.filter(
        (item) => item.id === props.items?.activityFactor
      )[0];
    } else {
      state.name = null;
      state.description = null;
      state.normPortions = 1;
      state.startDate = null;
      state.endDate = null;
      state.activityFactor = null;
    }
  }, 300);
});
</script>
