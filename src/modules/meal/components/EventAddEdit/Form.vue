<template>
  <div>
    <BaseField
      component="Select"
      label="Veranstaltung"
      techName="event"
      v-model="state.event"
      :errors="errors.event?.$errors"
      :items="events"
    />
    <BaseField
      component="Text"
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
      component="Number"
      label="Reserve-Faktor"
      techName="reserve_factor"
      v-model="state.reserveFactor"
      :errors="errors.reserveFactor?.$errors"
    />
    <BaseField
      component="Toggle"
      label="Öffentlich"
      techName="isPublic"
      v-model="state.isPublic"
      :errors="errors.isPublic?.$errors"
    />
    <BaseField
      component="Toggle"
      label="Verifiziert"
      techName="isApproved"
      v-model="state.isApproved"
      :errors="errors.isApproved?.$errors"
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
  event: null,
  description: '',
  normPortions: 1,
  activityFactor: 1.0,
  reserveFactor: 1.0,
  isPublic: false,
  isApproved: false,
});

const rules = {
  event: {
    required,
  },
  description: {
    required,
  },
  normPortions: {
    required,
  },
  activityFactor: {
    required,
  },
  reserveFactor: {
    required,
  },
  isPublic: {
    required,
  },
  isApproved: {
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

const events = computed(() => {
  return mealStore.events;
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
        event: state.event.id,
        description: state.description,
        normPortions: state.normPortions,
        activityFactor: state.activityFactor.id,
        reserveFactor: state.reserveFactor,
        isPublic: state.isPublic,
        isApproved: state.isApproved,
      })
      .then((response: any) => {
        debugger;
        goToRecipe(response.data.id);
      });
  } else {
    mealStore
      .updateEvent({
        id: state.id,
        event: state.event.id,
        description: state.description,
        normPortions: state.normPortions,
        activityFactor: state.activityFactor.id,
        reserveFactor: state.reserveFactor,
        isPublic: state.isPublic,
        isApproved: state.isApproved,
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

onMounted(async () => {
  await Promise.all([
    mealStore.fetchPhysicalActivity(),
    mealStore.fetchEvents(),
  ]);

  if (isEdit.value) {
    state.id = props.items?.id;
    state.description = props.items?.description;
    state.event = events.value.filter(
      (item) => item.id === props.items?.event?.id
    )[0];
    state.normPortions = props.items?.normPortions;
    state.activityFactor = physicalActivities.value.filter(
      (item) => item.id === props.items?.activityFactor
    )[0];
    state.reserveFactor = props.items?.reserveFactor;
    state.isPublic = props.items?.isPublic;
    state.isApproved = props.items?.isApproved;
  } else {
    state.event = null;
    state.normPortions = 1;
    state.activityFactor = physicalActivities.value[1];
    state.reserveFactor = 1;
    state.isPublic = false;
    state.isApproved = false;
  }
});
</script>
